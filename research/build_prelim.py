#!/usr/bin/env python3
"""One-time mechanical curation; the resulting packet has no dependency on this script."""
from __future__ import annotations
import ast
import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "prelim"
ARCHIVE = "artifacts/wilf_four_generators_review_package_2026-09-11/"

def text(path):
    return (ROOT / path).read_text()

def put(path, value):
    target = OUT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(value)

def extract(path, name):
    value = text(path)
    node = next(n for n in ast.parse(value).body if isinstance(n, ast.FunctionDef) and n.name == name)
    return "\n".join(value.splitlines()[node.lineno-1:node.end_lineno]) + "\n"

def copy_code():
    guard = """
int main(int argc, char**) {
    if (argc != 1) { std::cerr << "only complete mode supported\\n"; return 2; }
    try { for (int m = 20; m <= 29; ++m) run(m); }
    catch (const std::exception& error) { std::cerr << error.what() << '\\n'; return 1; }
    return 0;
}
"""
    for source, dest in (
        ("exhaust_small_multiplicity.cpp", "b1_residues.cpp"),
        ("independent_membership_check.cpp", "b1_membership.cpp"),
    ):
        value = text(ARCHIVE + "round5/small_multiplicity/" + source)
        value = value[:value.rindex("int main(")] + guard
        if "#include <limits>" not in value:
            value = "#include <limits>\n" + value
        value = value.replace("if (s.raw != ", 'if (s.negative || s.min_bounded_w < 0) throw std::runtime_error("finite predicate failed");\n    if (s.raw != ')
        value = value.replace("if(raw!=", 'if (negative || min_w < 0) throw std::runtime_error("finite predicate failed");\n    if(raw!=')
        value = re.sub(r"//[^\n]*(?:round[0-9]|R1[ab])[^\n]*\n", "", value)
        # Put width assertions after includes, before declarations.
        last_include = max(m.end() for m in re.finditer(r"^#include[^\n]*\n", value, re.M))
        value = value[:last_include] + """
static_assert(std::numeric_limits<long long>::digits >= 63, "64-bit scores required");
static_assert(std::numeric_limits<int>::digits >= 31, "32-bit indices required");
static_assert(std::numeric_limits<std::uint64_t>::digits == 64, "64-bit bitsets required");
""" + value[last_include:]
        put("code/" + dest, value)
    for source, name, dest, helper, imports in (
        ("verification/b2/check_interval_prefix.py", "prefix_bound", "b2_prefix.py", "require", ""),
        ("verification/b2/check_interval_direct.py", "explicit_bound", "b2_direct.py", "ensure",
         "from functools import lru_cache\nfrom itertools import product\nimport math\n"),
    ):
        put("code/" + dest, '"""Exact no-corner interval evaluator; no stored bounds are read."""\n'
            + "from __future__ import annotations\n" + imports
            + f"def {helper}(condition, message):\n    if not condition: raise RuntimeError(message)\n\n"
            + extract(source, name))
    value = text(ARCHIVE + "round5/one_corner_extension/corner_interval_worker.cpp")
    value = value[:value.rindex("int main(")]
    value = value.replace("#include <vector>", "#include <vector>\n#include <sstream>\n#include <stdexcept>\n#include <string>")
    value = value.replace("using I=long long;", """using I=long long;
static_assert(std::numeric_limits<I>::digits >= 63, "64-bit scores required");
static_assert(std::numeric_limits<int>::digits >= 31, "32-bit indices required");""")
    value += """
int main(int argc,char**) {
  std::ios::sync_with_stdio(false);std::cin.tie(nullptr);
  try {
    if(argc!=1)throw std::runtime_error("only complete mode supported");
    std::string line;
    while(std::getline(std::cin,line)) {
      I q;std::array<I,3>lo,hi;std::string extra;std::istringstream request(line);
      if(!(request>>q>>lo[0]>>lo[1]>>lo[2]>>hi[0]>>hi[1]>>hi[2])||(request>>extra))
        throw std::runtime_error("malformed request");
      if(q!=4096||lo[2]<6*q)throw std::runtime_error("unsupported scale or height");
      for(int i=0;i<3;++i)if(lo[i]<q||lo[i]>hi[i]||hi[i]>42*q)
        throw std::runtime_error("outside proved root");
      bool first=true;
      for(auto p:{std::array<int,3>{2,1,1},std::array<int,3>{1,2,1},std::array<int,3>{1,1,2}}) {
        I value=solve(q,lo,hi,p);
        if(value>q)throw std::runtime_error("finite predicate failed");
        if(!first)std::cout<<' ';first=false;std::cout<<value;
      }
      std::cout<<'\\n';
      if(!std::cout)throw std::runtime_error("output failure");
    }
    if(!std::cin.eof())throw std::runtime_error("input read failure");
  }catch(const std::exception& error){std::cerr<<error.what()<<'\\n';return 1;}
}
"""
    put("code/b4_high_prefix.cpp", value)
    copies = {
        "verification/b4/direct_clipped_worker.cpp": "b4_high_direct.cpp",
        "verification/b4/check_low_offsets.py": "b4_low_offsets.py",
        "verification/b4/check_low_successors.py": "b4_low_successors.py",
        "verification/b5/check_profiles_bits.cpp": "b5_bits.cpp",
        "verification/b5/check_profiles_columns.cpp": "b5_columns.cpp",
        "verification/b6/check_strip_prefix.cpp": "b6_strip_prefix.cpp",
        "verification/b6/check_strip_points.cpp": "b6_strip_points.cpp",
        "verification/b6/high_subtract.cpp": "b6_high_subtract.cpp",
        "verification/b6/high_disjoint.cpp": "b6_high_disjoint.cpp",
    }
    for source, dest in copies.items():
        value = text(source)
        if dest == "b4_high_direct.cpp":
            value = value.replace("int main() {", "int main(int argc,char**) {")
            value = value.replace("    try {\n", '    try {\n        if(argc!=1)throw std::runtime_error("only complete mode supported");\n', 1)
        value = re.sub(r"\bR4[ab]\b", "short-corner", value)
        value = re.sub(r"\bR6a\b", "strip", value)
        value = re.sub(r"\bR6b\b", "high-height", value)
        value = value.replace(", archive_inputs=False", "")
        put("code/" + dest, value)

def appendix():
    a = text("paper/central-box-horns.md").split("## 1. Statement", 1)[1].split("## 9. Retained interface", 1)[0]
    a = "## 1. Statement" + a
    a = re.sub(r"Thus the thickened sets in\n.*?belong to the same", "Thus the thickened sets of proof Section 4 belong to the same", a, flags=re.S)
    a = a.replace("height allowances, and interval bounds belong to the later B2 and B6\nspecifications rather than to G5.",
                  "height allowances, and interval bounds are specified in the proof spine.")
    b = text("paper/full-weighted-ideal.md").split("## 1. Setup and statement", 1)[1].split("## 6. Retained interface", 1)[0]
    b = "## 1. Setup and statement" + b
    c = text("paper/no-corner-compactness.md").split("## 2. Box-horn sets", 1)[1].split("This theorem is stated only", 1)[0]
    c = "## 2. Box-horn sets" + c
    degree = text("paper/no-corner-compactness.md").split("## 7. The degree-four cardinality bound", 1)[1].split("## 8. Proof", 1)[0]
    degree = degree.replace("Use the G5 decomposition", "Use the Appendix A decomposition")
    c += r"""
## 6. Application to the thickening

The rectangular thickening of proof Section 4, after positive diagonal
scaling, has the box-horn form proved in Appendix A. Its simplex containment
and the preceding theorem give its deficit at least one third.
The box side lengths named \(a,b,c\) in this appendix are local geometric
variables, not the semigroup conductor or normalized generator weights.

## 7. The degree-four cardinality bound
""" + degree
    def headings(value, letter):
        value = re.sub(r"^## (\d+)\. ", lambda m: f"### {letter}.{m[1]}. ", value, flags=re.M)
        value = re.sub(r"^### (Theorem|Lemma|Corollary|Remark)", r"#### \1", value, flags=re.M)
        return value.strip()
    put("analytic-details.md", """# Analytic details of the preliminary proof

These three appendices are integral parts of [the proof](proof.md).
Their equation and lemma numbers are local to each appendix.
Each establishes an analytic reduction without a finite computation.
All hypotheses required by the proof spine are stated here.

## Appendix A: central boxes and three monotone horns

The needed clique-tree fact is classical and is proved below.

""" + headings(a, "A") + "\n\n## Appendix B: full weighted Apéry ideals\n\n"
        + r"Here \(w(x)\) denotes the unnormalized integer label, locally to this appendix." + "\n\n"
        + headings(b, "B") + "\n\n## Appendix C: the continuous no-corner moment inequality\n\n"
        + headings(c, "C") + "\n")

def clip(low, high, component):
    low, high = list(low), list(high)
    for _ in range(20 if component == "b6" else 1):
        old = tuple(low), tuple(high)
        low = [low[0], max(low[:2]), max(low)]
        high = [min(high), min(high[1:]), high[2]]
        if any(a>b for a,b in zip(low, high)): return None
        if component == "b6":
            q = 4096
            ceil = lambda a,b: -(-a//b)
            cap = 9*q + ceil(28*q*q, low[2]-3*q)
            high[0] = min(high[0], ceil(cap-q, 2))
            high[1] = min(high[1], cap-q-low[0])
            high[2] = min(high[2], ceil(42*q+37*min(q+sum(high[:2]), cap), 5))
        if (tuple(low), tuple(high)) == old: break
    return None if any(a>b for a,b in zip(low,high)) else (tuple(low),tuple(high))

def trees():
    for component, manifest in (
        ("b2", "verification/b2/certificate-manifest.json"),
        ("b4", "verification/b4/certificate-manifest.json"),
        ("b6", "verification/b6/certificate-manifest.json"),
    ):
        origin = json.loads(text(manifest))
        raw = (ROOT / origin["certificate"]["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == origin["certificate"]["sha256"]
        old = json.loads(raw); nodes = old["tree"]; todo = [(0, tuple(map(tuple, old["initial"])))]; seen = set()
        compact = [None]*len(nodes)
        while todo:
            index, expected = todo.pop()
            assert index not in seen; seen.add(index)
            node = nodes[index]
            assert tuple(map(tuple,node["box"])) == expected
            tightened = clip(*expected, component)
            kind = node["kind"]
            if kind == "split":
                assert tightened is not None
                low, high = tightened
                axis, mid = node["axis"], node["mid"]
                assert low[axis] < mid < high[axis]
                left, right = list(high), list(low); left[axis] = right[axis] = mid
                a,b = node["children"]
                compact[index] = [axis,mid,a,b]
                todo.extend([(b,(tuple(right),high)),(a,(low,tuple(left)))])
            else:
                compact[index] = [{"empty":-1,"dp":-2,"continuous":-3,"planar":-3}[kind]]
                assert (tightened is None) == (kind=="empty")
        assert len(seen) == len(nodes) and all(n is not None for n in compact)
        result = dict(schema_version=1,component=component,scale=4096,root=old["initial"],nodes=compact)
        put("data/" + component + ".json", json.dumps(result,separators=(",",":"))+"\n")
        print(json.dumps(dict(component=component,nodes=len(nodes),bytes=(OUT/"data"/(component+".json")).stat().st_size,
                              topology_conversion_checked=True)))

def manifest():
    names = ["README.md","proof.md","analytic-details.md","verification.md","verify.py"]
    names += [str(p.relative_to(OUT)) for folder in ("code","data")
              for p in (OUT/folder).iterdir() if p.is_file()]
    entries = [dict(path=name,bytes=(OUT/name).stat().st_size,
                    sha256=hashlib.sha256((OUT/name).read_bytes()).hexdigest()) for name in sorted(names)]
    put("manifest.json",json.dumps(dict(schema_version=1,format="wilf-four-prelim-v1",inputs=entries),
                                  indent=2,sort_keys=True)+"\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest-only",action="store_true")
    args = parser.parse_args()
    if not args.manifest_only:
        copy_code()
        appendix()
        trees()
    manifest()
