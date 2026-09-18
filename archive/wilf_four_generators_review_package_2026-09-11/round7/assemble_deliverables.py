"""Assemble the dated report and a complete source/certificate archive.

The main overview controls scope. No incomplete experiment is promoted to a
theorem by being included in the archive.
"""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / 'deliverables'
MANUSCRIPT = DEST / 'wilf_four_generator_research_2026-09-10.md'
ARCHIVE = DEST / 'wilf_four_generator_proofs_and_certificates_2026-09-10.zip'

APPENDICES = [
 ('11 September proof synopsis and simplification', 'round8/review_synopsis.md'),
 ('Uniform rational certificates for the remaining low-height shapes', 'round8/simplification/low_height_sixmax_simplification.md'),
 ('Fresh structural proof with explicit median monotonicity', 'round8/audit_structure.md'),
 ('Fresh continuous and phase audit', 'round8/audit_phase.md'),
 ('Fresh low-height arithmetic and source audit', 'round8/audit_lowheight.md'),
 ('Fresh six-final-window and conductor audit', 'round8/audit_sixpoint.md'),
 ('Fresh high-height source audit and replay', 'round8/audit_computation.md'),
 ('The complete no-interior weighted theorem', 'round5/weight_arrangement/weighted_no_interior_theorem.md'),
 ('The complete short-corner weighted theorem', 'round5/one_corner_extension/short_corner_weighted_theorem.md'),
 ('Small multiplicities and the analytic finite reduction', 'round5/small_multiplicity/exhaustive_m20_m29_theorem.md'),
 ('All paired secondary semigroups', 'round5/secondary_quotients/no_interior_secondary_implication_audit.md'),
 ('The new continuous gap and strict multiplicity tail', 'round7/uniform_gap_theorem.md'),
 ('Independent uniform-gap audit', 'round7/uniform_gap_independent_audit.md'),
 ('Independent short-corner composition audit', 'round6/audit_short_corner.md'),
 ('Independent arithmetic exhaustion audit', 'round6/audit_enumerations.md'),
 ('Independent foundational audit', 'round6/audit_foundations.md'),
 ('The unbounded unit-weight theorem', 'round5/weighted_analytic/one_corner/unit_one_corner_theorem.md'),
 ('Arithmetic surface constraints and geometric obstructions', 'round7/global_step_audit.md'),
 ('The complete low-height theorem', 'round7/low_degree6/low_height_theorem.md'),
 ('Independent complete low-height coverage audit', 'round7/low_degree6/independent_coverage_audit.md'),
 ('The complete high-height theorem', 'round7/geometric_residual.md'),
 ('Independent high-height interval and worker audit', 'round7/geometric_residual/residual_interval_audit.md'),
 ('Independent disjoint-piece formulas and integer bounds', 'round7/geometric_residual/independent_specialized_piece_derivation.md'),
 ('Fresh mathematical audit of the six-point dependency', 'round7/six_point_fresh_math_audit.md'),
 ('Adversarial audit of the global composition', 'round7/final_composition_audit.md'),
 ('The type-reduction attempt and its exact obstruction', 'round7/type_reduction_attempt.md'),
]

ALLOWED = {'.md', '.py', '.cpp', '.hpp', '.h', '.js', '.json', '.jsonl', '.txt', '.tsv', '.bin'}

def main():
    DEST.mkdir(exist_ok=True)
    text = (ROOT/'round7/research_overview.md').read_text()
    for i, (title, name) in enumerate(APPENDICES, 1):
        p=ROOT/name
        if not p.is_file():
            raise FileNotFoundError(name)
        body=p.read_text()
        if body.startswith('# '): body=body.split('\n',1)[1].lstrip()
        text += f'\n\n---\n\n# Appendix {i}. {title}\n\n'
        text += f'Preserved source: `{name}`. Historical scope statements in this source\n'
        text += 'are read together with the dated overview and later composition audits.\n\n'
        text += body.rstrip()+'\n'
    MANUSCRIPT.write_text(text)

    entries={}
    prior_archive=ROOT/'deliverables/wilf_exact_proofs_and_certificates_2026-09-07.zip'
    with zipfile.ZipFile(prior_archive) as z:
        for name in z.namelist():
            if name.endswith('/') or name in {'README.md','MANIFEST.json'}: continue
            entries[name]=z.read(name)
    # Preserve the seed as well as its expanded contents so this assembler
    # remains runnable from an isolated extraction of its own output.
    entries[str(prior_archive.relative_to(ROOT))]=prior_archive.read_bytes()
    for part in ('round5','round6','round7','round8'):
        for p in (ROOT/part).rglob('*'):
            if not p.is_file() or any(x in {'__pycache__','deps','.git'} for x in p.parts): continue
            if p.suffix not in ALLOWED: continue
            # A compact basis certificate supersedes streamed diagnostic survivors.
            if p.name in {'survivors.tsv','sampled_survivors.tsv','weighted_candidates_sample.tsv'}: continue
            entries[str(p.relative_to(ROOT))]=p.read_bytes()
    for name in ('prior/wilf_edim4_six_point_and_column_theorems_2026-09-05.md',
                 'prior/wilf_edim4_six_point_verification_2026-09-05.zip',
                 'round2/arithmetic/general_interior_corner_bound.md',
                 'round3/no_interior/probe_slack_bridge.py'):
        entries[name]=(ROOT/name).read_bytes()
    entries['deliverables/'+MANUSCRIPT.name]=MANUSCRIPT.read_bytes()
    # The historical six-point manifest includes logs omitted from this
    # package and predates fresh timing records. Refresh only packaged bytes;
    # leave all historical workspace files unchanged.
    six_prefix='round7/six_point_dependency_replay/'
    six_manifest=six_prefix+'six-point-SHA256SUMS.json'
    six_readme=six_prefix+'README-six-point.md'
    readme=entries[six_readme].decode()
    readme=readme.replace(
        '`six-point-SHA256SUMS.json` records hashes of all other archive members.',
        '`six-point-SHA256SUMS.json` records hashes of all other files shipped '
        'in this subtree. It is refreshed when the dated archive is assembled.')
    entries[six_readme]=readme.encode()
    entries[six_manifest]=(json.dumps({
        name[len(six_prefix):]:hashlib.sha256(data).hexdigest()
        for name,data in sorted(entries.items())
        if name.startswith(six_prefix) and name!=six_manifest
    },indent=2)+'\n').encode()
    entries['README.md']=('''# Four-generator Wilf: proof sources and certificates — revised 11 September 2026

Read `deliverables/'''+MANUSCRIPT.name+'''` first. Its dated scope
states the complete four-generator argument and distinguishes its proof
dependencies from diagnostic work. All final certificate gates have passed;
external mathematical review and proof-assistant formalization are outstanding.

The archive preserves proof sources and exact computation records. Inclusion
does not turn a failed or incomplete experiment into a universal certificate.
Historical conditional statements must be read with their later audits.

The 11 September review is in `round8/review_synopsis.md`. It records the
additional 380,607 independently verified low-height duals, so that all
3,742,041 surviving residual shapes now have the same rational certificate.
The separate (1,1,1) corner still uses the six-final-window theorem.

Run these core reproduction commands from the extracted archive root
(Python 3, Node.js, and C++17; do not disable Python assertions):

```
python3 round4/verify_completed_results.py
node round7/verify_uniform_gap.js
python3 round5/weight_arrangement/verify_interval_certificate.py
python3 round5/structural_audit/verify_complete_short_corner.py
python3 round5/interior_arithmetic/verify_low_height_weighted.py
python3 round5/small_multiplicity/verify_exhaustion.py --rerun
python3 round5/secondary_quotients/verify_secondary_implications.py
python3 round7/global_step/verify_surface_identities.py
python3 round7/low_degree6/verify_complete_certificate.py
python3 round8/simplification/verify_certificate.py
python3 round7/geometric_residual/verify_residual_certificate.py --certificate round7/geometric_residual/residual_parallel_interval_certificate.json --worker specialized --jobs 8
python3 round7/verify_type_fixture.py
```

The high-height command above uses no cache and freshly recomputes all
47,088 accepted leaves. The frozen certificate has SHA-256
`173fe6ec196b3d2adabad313749482542ad3492b5f6b4e398e76bbe6e52e405c`.
The saved report `independent_full_tree_replay_47088_checks.json` in that
directory records the first complete observed independent replay. Historical
prefixes and checkpoints are not substitutes for this final certificate.

The independent rational verification does not require the floating-point
optimizers used to propose certificates. Some exploratory scripts do require
SciPy/NumPy. A complete fresh replay of the older six-point dependency uses
SciPy for discovery; its runner changes to its own working directory:

```
python3 round7/six_point_dependency_replay/run_six_point_verification.py
```

To check the stored six-point rational certificates using only Python's
standard library, first change to that subtree:

```
cd round7/six_point_dependency_replay
python3 verify_six_certificates.py
python3 verify_corner_completion.py
python3 wilf_column_bound.py
```

The complete unit-weight one-corner result is separately reproducible from
the archive root with
`python3 round5/weighted_analytic/one_corner/verify_unit_one_corner_theorem.py`.

MANIFEST.json records the SHA-256 digest of every included payload. Replays
may regenerate timing records. Compiled executables and third-party library
installations are excluded. Binary files, when present, are exact witness
indices, not executable code.
''').encode()
    entries['MANIFEST.json']=(json.dumps({'files':{
        name:hashlib.sha256(data).hexdigest() for name,data in sorted(entries.items())
    }},indent=2)+'\n').encode()
    with zipfile.ZipFile(ARCHIVE,'w',zipfile.ZIP_DEFLATED) as z:
        for name,data in sorted(entries.items()): z.writestr(name,data)
    print(json.dumps({'manuscript':str(MANUSCRIPT),'manuscript_bytes':MANUSCRIPT.stat().st_size,
                      'archive':str(ARCHIVE),'archive_bytes':ARCHIVE.stat().st_size,
                      'archive_files':len(entries)},indent=2))

if __name__=='__main__': main()
