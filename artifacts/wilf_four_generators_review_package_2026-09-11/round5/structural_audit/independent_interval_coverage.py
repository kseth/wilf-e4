"""Third-party exact audit of the complete interval partition tree."""
import json
from pathlib import Path
from collections import deque, Counter
from independent_interval_dp import tighten


def audit(path):
    cert = json.loads(Path(path).read_text())
    q = cert['scale']
    root = [[q, q, 5*q], [24*q, 24*q, 24*q]]
    assert cert['initial'] == root
    assert cert['complete'] and cert['unresolved'] == []
    tree = cert['tree']
    frontier = deque([(0, root)])
    seen = set()
    counts = Counter()
    while frontier:
        identifier, wanted = frontier.popleft()
        assert isinstance(identifier, int) and 0 <= identifier < len(tree)
        assert identifier not in seen
        seen.add(identifier)
        node = tree[identifier]
        assert node['box'] == wanted
        clipped = tighten(*wanted)
        kind = node['kind']
        counts[kind] += 1
        if clipped is None:
            assert kind == 'empty'
            continue
        assert kind in ('split', 'dp', 'continuous')
        if kind != 'split':
            continue
        lower, upper = map(list, clipped)
        axis, mid = node['axis'], node['mid']
        assert axis in (0, 1, 2)
        assert isinstance(mid, int) and lower[axis] < mid < upper[axis]
        children = node['children']
        assert len(children) == 2 and children[0] != children[1]
        left_upper = upper.copy()
        right_lower = lower.copy()
        left_upper[axis] = right_lower[axis] = mid
        frontier.append((children[0], [lower, left_upper]))
        frontier.append((children[1], [right_lower, upper]))
    assert len(seen) == len(tree) == cert['nodes']
    assert sum(value for key, value in counts.items() if key != 'split') == cert['leaf_count']
    return {'status': 'PASS', 'scope': 'complete closed-box coverage of 1<=b<=c<=M, 5<=M<=24',
            'nodes': len(tree), 'node_kinds': dict(counts), 'scale': q}


if __name__ == '__main__':
    result = audit('round5/weight_arrangement/full_interval_certificate.json')
    Path('round5/structural_audit/independent_interval_coverage_results.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))
