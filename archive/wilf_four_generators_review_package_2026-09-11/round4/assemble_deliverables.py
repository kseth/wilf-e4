"""Build the dated manuscript and reproducible source archive."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / 'deliverables'
STEM = 'wilf_no_interior_theorem_and_remaining_cases_2026-09-07'
MANUSCRIPT = DEST / (STEM + '.md')
ARCHIVE = DEST / 'wilf_exact_proofs_and_certificates_2026-09-07.zip'


def read(path):
    return (ROOT / path).read_text()


def appendix(label, title, source, start=None, end=None, preface=''):
    content = read(source)
    if start is not None:
        content = content[content.index(start):]
    if end is not None:
        content = content[:content.index(end)]
    if content.startswith('# '):
        content = content.split('\n', 1)[1].lstrip()
    return ('\n\n---\n\n# Appendix ' + label + '. ' + title + '\n\n'
            + preface + '\n\n' + content.strip() + '\n')


def main():
    DEST.mkdir(exist_ok=True)
    text = read('round4/research_overview.md')
    text += appendix('A', 'The clique-tree and three-arm decomposition',
        'round3/no_interior/clique_tree_and_bipartite_bound.md',
        start='## 1. A chordal graph', end='## 4. The bipartite',
        preface='This structural argument is retained from the preceding checkpoint. '
                'Its former references to an unproved mean bound are superseded by '
                'Appendices D–E; no change to the structural hypotheses is needed.')
    text += appendix('B', 'Exact optimization of boundary horns',
        'round3/horns_optimization/fullcap_boundary_theorem.md',
        start='## 1. Exact optimization', end='## 3. The canonical',
        preface='The formulas below use maximum height one. Positive scaling gives '
                'the height-M formula in Appendix E. The earlier full-cap theorem '
                'is also preserved in the source archive.')
    text += appendix('C', 'Endpoint convexity and the late-horn theorem',
        'round3/descent/late_horn_potential.md',
        end='## 4. An exact obstruction')
    text += appendix('D', 'The arbitrary-horn bridge',
        'round4/bellman/arbitrary_horn_bridge.md')
    text += appendix('E', 'The joint effective-cap theorem',
        'round4/joint_horns/joint_effective_cap_theorem.md')
    text += appendix('F', 'The exact discrete phase estimate',
        'deliverables/wilf_fixed_dimension_finite_reduction_2026-09-05.md',
        start='# Sharper discrete phase estimate',
        end='On the other hand,\n\\[\nm\\le',
        preface='For a normalized finite lower ideal, let μ_i=E[u_i X_i] and '
                'let δ_i be one minus the weight of the top of the i-coordinate '
                'fiber through X. Conditional uniformity gives '
                'Eδ_i=1−E[u·X]−μ_i. Summing yields Σ_i Eδ_i=κ, and hence '
                'μ_i=(1+κ)/4−Eδ_i. These exact identities justify the uses below.')
    text += appendix('G', 'The multiplicity bound 1836',
        'round4/discrete/conditional_discrete_bridge.md')
    text += appendix('H', 'The unit-weight integer theorem and weighted scope',
        'round4/discrete_horns/discrete_horn_results.md')
    text += appendix('I', 'The secondary quotient ⟨3,4,5⟩',
        'round4/secondary/ordinary_three_theorem.md')
    text += appendix('J', 'The secondary family ⟨3,3g+1,3g+2⟩',
        'round4/secondary/quotient_three_progression_theorem.md')
    text += appendix('K', 'Composition audit and the quotient-conductor bound 40',
        'round4/audit/composition_audit.md')
    text += appendix('L', 'An exact obstruction to the one-corner extension',
        'round4/audit/one_corner_extension_obstruction.md')
    text += appendix('M', 'Unavoidable corners and residue-tiling constraints',
        'round4/audit/lex_order_and_tiling_obstructions.md')
    text += appendix('N', 'Why equalizing weights does not finish the proof',
        'round4/discrete_horns/unequal_exposed_vertex.md')
    MANUSCRIPT.write_text(text)

    dependencies = [
        'round3/no_interior/clique_tree_and_bipartite_bound.md',
        'round3/horns_optimization/fullcap_boundary_theorem.md',
        'round3/horns_optimization/fullcap_boundary_verify.py',
        'round3/horns_optimization/fullcap_boundary_verification.json',
        'round3/descent/late_horn_potential.md',
        'round3/descent/horns_audit.md',
        'round3/gcd_and_extension_reductions.md',
        'round3/secondary/quotient_two_exact_formulas.md',
        'round2/type/secondary_structure_report.md',
        'round2/amplification/general_dimension.md',
        'deliverables/wilf_edim4_global_finite_reduction_2026-09-05.md',
        'deliverables/wilf_edim4_global_finite_reduction_checks_2026-09-05.zip',
        'deliverables/wilf_fixed_dimension_finite_reduction_2026-09-05.md',
        'deliverables/wilf_fixed_dimension_finite_reduction_checks_2026-09-05.zip',
        'deliverables/wilf_secondary_family_and_remaining_gaps_2026-09-05.md',
        'deliverables/wilf_secondary_family_exact_certificates_2026-09-05.zip',
    ]
    entries = {}
    for path in (ROOT / 'round4').rglob('*'):
        if not path.is_file() or any(p in ('deps', '__pycache__') for p in path.parts):
            continue
        if path.suffix not in ('.md', '.py', '.json'):
            continue
        entries[str(path.relative_to(ROOT))] = path.read_bytes()
    for name in dependencies:
        entries[name] = (ROOT / name).read_bytes()
    entries['deliverables/' + MANUSCRIPT.name] = MANUSCRIPT.read_bytes()
    entries['README.md'] = ('''# Wilf exact proofs and certificates, 7 September 2026

Read deliverables/''' + MANUSCRIPT.name + ''' for the report and full proofs.

The unrestricted four-generator conjecture remains unresolved by this work.
Completed: the continuous no-interior mean theorem, the subclass bound 1836,
the equal-weight integer theorem, and the stated secondary quotient family.

Run `python3 round4/verify_completed_results.py` from the extracted archive.
Its exact certificate checks require only the Python standard library.
The checks establish finite identities and recurrences used in the proofs;
the analytic arguments also require reading the manuscript and audit notes.
The runner does not enumerate all remaining numerical semigroups.

Files described as probes, searches, or diagnostics are bounded experiments,
not universal certificates. Some require NumPy, SciPy, or SymPy. They are
not called by the proof-certificate runner. Third-party installations are
excluded. Historical checkpoint archives are included in deliverables/ to
preserve the earlier proofs and their exact scripts without replacing them.
Older notes may call a formerly missing implication "unproved" or
"conditional"; the dated main report states which are now completed.

MANIFEST.json contains SHA-256 hashes of the archived content. Rerunning
checkers may regenerate JSON outputs (including timing data).
''').encode()
    manifest = {'files': {name: hashlib.sha256(data).hexdigest()
                          for name, data in sorted(entries.items())}}
    entries['MANIFEST.json'] = (json.dumps(manifest, indent=2) + '\n').encode()
    with zipfile.ZipFile(ARCHIVE, 'w', zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(entries.items()):
            archive.writestr(name, data)
    print(json.dumps({'manuscript': str(MANUSCRIPT),
                      'manuscript_bytes': MANUSCRIPT.stat().st_size,
                      'archive': str(ARCHIVE),
                      'archive_bytes': ARCHIVE.stat().st_size,
                      'archive_files': len(entries)}, indent=2))


if __name__ == '__main__':
    main()
