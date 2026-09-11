"""Run the finite exact certificates supporting the completed round-four results.

Run from any directory with Python 3. No third-party modules are required.
Analytic steps must also be read in the accompanying manuscript; this runner
does not prove unrestricted Wilf or exhaust the remaining semigroups.
"""
from pathlib import Path
import json
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = [
    "round3/horns_optimization/fullcap_boundary_verify.py",
    "round4/bellman/verify_horn_bridge_identities.py",
    "round4/joint_horns/verify_joint_effective_caps.py",
    "round4/discrete/max_no_interior_size.py",
    "round4/discrete/verify_conditional_discrete_bridge.py",
    "round4/discrete_horns/unit_weight_dp.py",
    "round4/secondary/ordinary_three_certificate.py",
    "round4/secondary_audit/verify_ordinary_three.py",
    "round4/secondary/quotient_three_progression_certificate.py",
    "round4/secondary_audit/verify_quotient_three_progression.py",
    "round4/audit/one_corner_extension_check.py",
    "round4/audit/lex_order_and_tiling_check.py",
    "round4/discrete_horns/verify_unequal_exposed_vertex.py",
]


def main():
    records = []
    for script in SCRIPTS:
        started = time.monotonic()
        result = subprocess.run(
            [sys.executable, str(ROOT / script)], cwd=ROOT,
            capture_output=True, text=True, timeout=120,
        )
        record = {
            "script": script,
            "passed": result.returncode == 0,
            "return_code": result.returncode,
            "elapsed_seconds": round(time.monotonic() - started, 3),
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
        records.append(record)
        print(("PASS " if record["passed"] else "FAIL ") + script, flush=True)
        if not record["passed"]:
            print(result.stdout)
            print(result.stderr, file=sys.stderr)
            break
    output = {
        "scope": "Exact finite certificates and obstruction checks; not unrestricted Wilf",
        "all_passed": len(records) == len(SCRIPTS) and all(r["passed"] for r in records),
        "third_party_dependencies": [],
        "records": records,
    }
    (ROOT / "round4/verification_results.json").write_text(json.dumps(output, indent=2) + "\n")
    if not output["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
