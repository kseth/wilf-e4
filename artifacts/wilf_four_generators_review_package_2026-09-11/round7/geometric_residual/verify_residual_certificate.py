#!/usr/bin/env python3
"""Independent closed-tree coverage and all-corner DP replay.

The clipping code does not import the generating script. Rational bounds are
constructed with Fraction and rounded outward at each documented step.
Use --sample 100 for a bounded replay; omit --sample for all DP leaves.
Use --checkpoint only to inspect a partial generator tree, never as a proof.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

ROOT = Path(__file__).resolve().parent


def ceiling(x):
    assert isinstance(x, F)
    return x.numerator // x.denominator + bool(x.numerator % x.denominator)


def outward_clip(box, scale):
    lower, upper = [list(v) for v in box]
    assert len(lower) == len(upper) == 3
    for unused in range(20):
        previous = (tuple(lower), tuple(upper))
        lower = [lower[0], max(lower[:2]), max(lower)]
        upper = [min(upper), min(upper[1:]), upper[2]]
        if any(a > b for a, b in zip(lower, upper)):
            break
        assert lower[2] > 3 * scale
        phase_sum = F(9) + F(28) / (F(lower[2], scale) - 3)
        # First replace the strict phase bound by an outward grid bound.
        phase_sum = F(ceiling(phase_sum * scale), scale)
        upper[0] = min(upper[0], ceiling(scale * (phase_sum - 1) / 2))
        upper[1] = min(upper[1], ceiling(scale * (phase_sum - 1 - F(lower[0], scale))))
        sum_bound = min(phase_sum, 1 + F(upper[0] + upper[1], scale))
        upper[2] = min(upper[2], ceiling(scale * (42 + 37 * sum_bound) / 5))
        if previous == (tuple(lower), tuple(upper)):
            break
    return tuple(lower), tuple(upper)


def as_box(box):
    return tuple(tuple(x) for x in box)


def inspect_tree(data, checkpoint=False):
    scale = data['scale']
    assert scale == 4096
    initial = as_box(data['initial'])
    assert initial == ((scale, scale, 7 * scale), (78 * scale,) * 3)
    tree = data['tree']
    pending = {index: as_box(box) for box, index in data.get('stack', [])}
    if not checkpoint:
        assert data['complete'] is True
        assert not pending and not data.get('unresolved')
    todo = [(0, initial)]
    seen = set()
    leaves = []
    counts = {'split': 0, 'dp': 0, 'empty': 0, 'pending': 0, 'unresolved': 0}
    while todo:
        index, expected = todo.pop()
        assert index not in seen and 0 <= index < len(tree)
        seen.add(index)
        row = tree[index]
        if row is None:
            assert checkpoint and pending[index] == expected
            counts['pending'] += 1
            continue
        assert as_box(row['box']) == expected
        clipped = outward_clip(expected, scale)
        lo, hi = clipped
        empty = any(a > b for a, b in zip(lo, hi))
        kind = row['kind']
        assert kind in counts
        counts[kind] += 1
        if kind == 'empty':
            assert empty
            continue
        assert not empty
        if kind == 'dp':
            bounds = row['bounds']
            assert len(bounds) == 6 and bounds[5] == 1
            assert 10 * bounds[0] <= 29 * scale
            leaves.append((index, clipped, bounds))
        elif kind == 'split':
            axis, mid = row['axis'], row['mid']
            assert axis in range(3) and lo[axis] < mid < hi[axis]
            left_hi = list(hi)
            left_hi[axis] = mid
            right_lo = list(lo)
            right_lo[axis] = mid
            children = row['children']
            assert len(children) == 2 and children[0] != children[1]
            todo.append((children[1], (tuple(right_lo), hi)))
            todo.append((children[0], (lo, tuple(left_hi))))
        elif kind == 'unresolved':
            assert checkpoint
        else:
            raise AssertionError(kind)
    assert len(seen) == len(tree)
    assert counts['pending'] == len(pending)
    return counts, leaves


def replay_batch(exe, leaves, scale, job, cache_stream=None, cache_lock=None, original_tree=None, worker_hash=None):
    tested = 0
    corner_cases = 0
    start = time.time()
    with subprocess.Popen([str(exe)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, bufsize=1) as worker:
        for index, (lo, hi), bounds in leaves:
            worker.stdin.write(' '.join(map(str, (scale, *lo, *hi))) + '\n')
            worker.stdin.flush()
            replay = list(map(int, worker.stdout.readline().split()))
            assert len(replay) == 5
            assert replay[0] == bounds[0], (index, replay, bounds)
            assert 10 * replay[0] <= 29 * scale
            # All Cartesian corner candidates are replayed without symmetry pruning.
            assert replay[4] >= bounds[4]
            if cache_stream is not None:
                record = dict(index=index, original_box=original_tree[index]['box'],
                              clipped=[lo, hi], bound=replay[0], corner_cases=replay[4],
                              worker_source_sha256=worker_hash)
                with cache_lock:
                    # Reopen for each record: a long-lived descriptor can refer
                    # to an older inode if workspace synchronization replaces it.
                    with cache_stream.open('a') as output:
                        output.write(json.dumps(record, separators=(',', ':')) + '\n')
            tested += 1
            corner_cases += replay[4]
            if tested % 1000 == 0:
                print(json.dumps({'job': job, 'leaves': tested, 'corner_cases': corner_cases,
                                  'seconds': time.time()-start}), flush=True)
        worker.stdin.close()
        assert worker.wait() == 0
    return tested, corner_cases


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sample', type=int, default=0)
    parser.add_argument('--checkpoint', action='store_true')
    parser.add_argument('--coverage-only', action='store_true')
    parser.add_argument('--jobs', type=int, default=1)
    parser.add_argument('--certificate', type=Path)
    parser.add_argument('--cache', type=Path,
                        help='Resume previously verified matching leaves; append new exact replay records.')
    parser.add_argument('--worker', choices=('pieces', 'points', 'specialized'), default='pieces')
    args = parser.parse_args()
    assert args.jobs >= 1
    name = 'residual_certificate_checkpoint.json' if args.checkpoint else 'residual_interval_certificate.json'
    path = args.certificate or ROOT / name
    content = path.read_bytes()
    data = json.loads(content)
    counts, leaves = inspect_tree(data, args.checkpoint)
    print(json.dumps({'tree_coverage': 'PASS', 'scope': 'partial checkpoint' if args.checkpoint else 'complete tree',
                      'counts': counts}), flush=True)
    leaves.sort()
    if args.sample and len(leaves) > args.sample:
        leaves = [leaves[i * (len(leaves)-1) // (args.sample-1)] for i in range(args.sample)] if args.sample > 1 else [leaves[0]]
    tested = 0
    corner_cases = 0
    cached_count = 0
    cached_cases = 0
    start = time.time()
    if not args.coverage_only:
        base = {'pieces': 'independent_residual_worker',
                'points': 'independent_residual_point_worker',
                'specialized': 'independent_specialized_piece_worker'}[args.worker]
        exe = ROOT / base
        source = ROOT / (base + '.cpp')
        worker_hash = hashlib.sha256(source.read_bytes()).hexdigest()
        allowed_worker_hashes = {hashlib.sha256((ROOT / file).read_bytes()).hexdigest()
                                for file in ('independent_residual_worker.cpp', 'independent_residual_point_worker.cpp',
                                             'independent_specialized_piece_worker.cpp')}
        if not exe.exists() or exe.stat().st_mtime < source.stat().st_mtime:
            subprocess.run(['g++', '-O3', '-std=c++17', str(source), '-o', str(exe)], check=True)
        cached = {}
        if args.cache and args.cache.exists():
            for line in args.cache.read_text().splitlines():
                record = json.loads(line)
                assert record['index'] not in cached
                cached[record['index']] = record
            if not args.checkpoint:
                # A resumed prefix must still be an identical set of final-tree leaves.
                for index, record in cached.items():
                    assert 0 <= index < len(data['tree'])
                    final_row = data['tree'][index]
                    assert final_row['kind'] == 'dp'
                    assert as_box(final_row['box']) == as_box(record['original_box'])
                    assert outward_clip(final_row['box'], data['scale']) == as_box(record['clipped'])
                    assert final_row['bounds'][0] == record['bound']
        remaining = []
        for index, clipped, bounds in leaves:
            if index not in cached:
                remaining.append((index, clipped, bounds))
                continue
            record = cached[index]
            assert record['worker_source_sha256'] in allowed_worker_hashes
            assert as_box(record['original_box']) == as_box(data['tree'][index]['box'])
            assert as_box(record['clipped']) == clipped
            assert record['bound'] == bounds[0] and 10 * record['bound'] <= 29 * data['scale']
            assert record['corner_cases'] >= bounds[4]
            cached_count += 1
            cached_cases += record['corner_cases']
        leaves = remaining
        cache_stream = args.cache
        cache_lock = Lock()
        try:
            with ThreadPoolExecutor(max_workers=args.jobs) as pool:
                futures = [pool.submit(replay_batch, exe, leaves[job::args.jobs], data['scale'], job,
                                       cache_stream, cache_lock, data['tree'], worker_hash)
                           for job in range(args.jobs)]
                for completed in as_completed(futures):
                    count, cases = completed.result()
                    tested += count
                    corner_cases += cases
        finally:
            pass
    if not args.sample and not args.coverage_only:
        assert tested + cached_count == counts['dp']
    result = dict(status='PASS', scope='partial checkpoint' if args.checkpoint else 'complete tree',
                  certificate_sha256=hashlib.sha256(content).hexdigest(),
                  coverage=counts, dp_leaves_replayed=tested,
                  independent_corner_cases=corner_cases, sampled=bool(args.sample),
                  cached_verified_leaves=cached_count, cached_corner_cases=cached_cases,
                  total_verified_leaves=tested+cached_count,
                  selected_worker=args.worker,
                  coverage_only=args.coverage_only, seconds=time.time()-start)
    suffix = 'checkpoint' if args.checkpoint else 'complete'
    if args.sample:
        suffix += '_sample'
    if args.coverage_only:
        suffix += '_coverage'
    (ROOT / ('independent_residual_' + suffix + '_checks.json')).write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
