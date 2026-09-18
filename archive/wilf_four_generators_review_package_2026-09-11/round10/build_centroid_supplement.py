#!/usr/bin/env python3
"""Package stable centroid proofs, sources, certificates, and audit records."""
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "deliverables/wilf_centroid_local_constructions_checks_2026-09-11.zip"
ALLOWED = {".py", ".cpp", ".hpp", ".md", ".json", ".jsonl", ".gz", ".txt", ".tsv"}
payloads = {
    p.relative_to(ROOT).as_posix(): p
    for p in (ROOT/"round10").rglob("*")
    if p.is_file() and p.suffix in ALLOWED
    and "__pycache__" not in p.parts
    and p.name not in {"package_verification.json"}
}
for name in (
    "deliverables/wilf_centroid_local_constructions_2026-09-11.md",
    "round7/low_degree6/low_height_theorem.md",
    "round7/global_step_audit.md",
):
    payloads[name] = ROOT / name

# Confirm both final mathematical payload manifests before packaging.
local = ROOT/"round10/local_centroid"
local_manifest = json.loads((local/"local_centroid_manifest.json").read_text())
for name, wanted in local_manifest["files"].items():
    assert hashlib.sha256((local/name).read_bytes()).hexdigest() == wanted, name
envelope = ROOT/"round10/envelope"
env_manifest = json.loads((envelope/"artifact_manifest.json").read_text())
for name, wanted in env_manifest["files"].items():
    data = (envelope/name).read_bytes()
    assert len(data) == wanted["bytes"], name
    assert hashlib.sha256(data).hexdigest() == wanted["sha256"], name
local_run = json.loads((local/"portable_replay_result.json").read_text())
env_run = json.loads((envelope/"universal_envelope_independent_result.json").read_text())
assert local_run["status"] == env_run["status"] == "passed"
assert local_run["total_shapes"] == 5574644
assert local_run["axis_fallbacks"] == 431
assert env_run["parameter_cases"] == 44281
assert env_run["moment_certificates"] + env_run["cardinality_certificates"] == 44281

manifest = {}
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for name, path in sorted(payloads.items()):
        data = path.read_bytes()
        manifest[name] = {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
        archive.writestr(name, data)
    archive.writestr("MANIFEST_SHA256.json", json.dumps(manifest, indent=2)+"\n")
with zipfile.ZipFile(OUT) as archive:
    assert archive.testzip() is None
    observed = json.loads(archive.read("MANIFEST_SHA256.json"))
    assert set(archive.namelist()) == set(observed) | {"MANIFEST_SHA256.json"}
    for name, expected in observed.items():
        data = archive.read(name)
        assert len(data) == expected["bytes"], name
        assert hashlib.sha256(data).hexdigest() == expected["sha256"], name
result = {
    "status": "passed",
    "payloads": len(manifest),
    "archive_bytes": OUT.stat().st_size,
    "archive_sha256": hashlib.sha256(OUT.read_bytes()).hexdigest(),
    "all_payload_hashes_checked": True,
    "both_final_proof_manifests_checked": True,
    "observed_local_replay_shapes": local_run["total_shapes"],
    "observed_envelope_replay_cells": env_run["parameter_cases"],
    "full_mathematical_replay_during_packaging": False,
}
(ROOT/"round10/package_verification.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
