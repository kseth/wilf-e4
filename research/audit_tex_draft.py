"""Editorial TeX/PRELIM fidelity and build audit, not a proof checker.

Run after `make pdf` in manuscript/. Requires Poppler's pdftotext.
The proof spine and analytic mathematics are compared. Implementation
arithmetic envelopes remain in PRELIM rather than the revised manuscript.
This does not verify deductions or establish any computational premise.
"""
from pathlib import Path
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "manuscript"


def require(condition, message):
    if not condition:
        raise SystemExit("FAIL: " + message)


def read(name):
    return (PAPER / name).read_text(encoding="utf-8")


def expressions(text, display):
    if display:
        matches = re.findall(
            r"\\\[(.*?)\\\]|\\begin\{equation\}(.*?)\\end\{equation\}",
            text, re.S,
        )
        values = [a or b for a, b in matches]
    else:
        values = re.findall(r"\\\((.*?)\\\)", text, re.S)
        values = [v for v in values if v != r"\square"]
    return [re.sub(r"\s+", "", re.sub(r"\\(?:tag|label)\{[^}]*\}", "", v))
            for v in values]


def without_tagged_displays(source, tags):
    """Remove only explicitly approved duplicated PRELIM derivations."""
    removed = {tag: 0 for tag in tags}

    def replace(match):
        for tag in tags:
            if r"\tag{" + tag + "}" in match.group(1):
                removed[tag] += 1
                return ""
        return match.group(0)

    source = re.sub(r"\\\[(.*?)\\\]", replace, source, flags=re.S)
    require(all(count == 1 for count in removed.values()),
            "an approved duplicated display is missing or repeated")
    return source


spine = (ROOT / "prelim/proof.md").read_text(encoding="utf-8")
spine = spine[spine.index("## 1. "):
              spine.index("All finite predicates are exact integer comparisons.")]
spine = re.sub(r"^> ?", "", spine, flags=re.M)
# The interval and strip displays now cite the one recurrence in Appendix A.
spine = without_tagged_displays(spine, {"14", "23"})
analytic = (ROOT / "prelim/analytic-details.md").read_text(encoding="utf-8")
b = analytic.index("## Appendix B:")
c = analytic.index("## Appendix C:")
# The only mathematical notation change in the import is local w(x) -> lambda(x).
analytic = analytic[:b] + analytic[b:c].replace("w(", r"\lambda(") + analytic[c:]

# The overflow envelopes are implementation documentation, not part of the
# selected mathematical proof. They are preserved in the frozen packet.
selected = {"spine": (spine, read("proof.tex")),
            "analytic": (analytic, read("analytic.tex"))}
fidelity = {}
for name, (original, tex) in selected.items():
    fidelity[name] = {}
    for display in (True, False):
        expected, actual = expressions(original, display), expressions(tex, display)
        kind = "displays" if display else "inline"
        require(expected == actual, f"{name} {kind} differ from selected PRELIM")
        fidelity[name][kind] = len(actual)

main = read("main.tex")
includes = re.findall(r"\\input\{([^}]+)\}", main)
require(includes == ["introduction", "proof", "analytic", "verification",
                     "extensions", "related", "construction"],
        "document order differs from the requested structure")
sources = [main] + [read(name + ".tex") for name in includes]
all_tex = "\n".join(sources)
require(not any(re.search(r"\\input\{|\\include\{", s) for s in sources[1:]),
        "an unexpected secondary source dependency appeared")
require("artifacts/" not in all_tex and "../paper/" not in all_tex,
        "historical proof dependencies appeared")
require(not re.search(r"\\(?:sub)*section\{[^}]*responsibility", all_tex, re.I),
        "a separate responsibility section appeared")
require("GPT-6 Astra" in read("construction.tex"), "initial AI history missing")
require("GPT-5.6 Sol" in read("construction.tex") and
        "via Codex" in read("construction.tex"), "reconstruction AI history missing")

labels = re.findall(r"\\label\{([^}]+)\}", all_tex)
require(len(labels) == len(set(labels)), "duplicate TeX labels")
refs = re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", all_tex)
require(set(refs) <= set(labels), "undefined source cross-reference")
cites = set()
for group in re.findall(r"\\cite(?:\[[^\]]*\])?\{([^}]+)\}", all_tex):
    cites.update(group.split(","))
bibkeys = re.findall(r"@\w+\{([^,]+),", read("references.bib"))
require(len(bibkeys) == len(set(bibkeys)), "duplicate bibliography keys")
require(cites == set(bibkeys), "missing or unused bibliography entries")
require(len(cites) == 15, "unexpected bibliography inventory")
require(len(re.findall(r"\\begin\{finitelemma\}", all_tex)) == 7,
        "the seven selected finite assertions changed")

for source in sources:
    environments = re.findall(r"\\(begin|end)\{([^}]+)\}", source)
    stack = []
    for action, env in environments:
        if action == "begin":
            stack.append(env)
        else:
            require(bool(stack) and stack.pop() == env, "unbalanced TeX environment")
    require(not stack, "unclosed TeX environment")

log = read("build/main.log")
require(not re.search(r"Warning:|Overfull|Underfull|undefined|Fatal error", log),
        "the converged TeX build contains a warning or layout error")
blg = read("build/main.blg")
require(not re.search(r"Warning--|error message", blg), "BibTeX diagnostics")
pdf = PAPER / "wilf-four-generators.pdf"
require(pdf.read_bytes() == (PAPER / "build/main.pdf").read_bytes(),
        "the reader PDF differs from the latest build")
result = subprocess.run(["pdftotext", "-layout", str(pdf), "-"],
                        text=True, capture_output=True, check=True)
text = result.stdout
require(not result.stderr and "??" not in text, "PDF extraction or unresolved reference")
headings = ["Extensions to embedding dimension greater than four",
            "Related work", "How the proof was constructed", "References"]
proof_heading = re.search(r"(?m)^2\s+Proof of the four-generator inequality\s*$", text)
require(proof_heading is not None, "PDF proof heading is missing")
body = text[proof_heading.start():]
require(all(h in body for h in headings), "a requested PDF section is missing")
require(text.count("Finite lemma 2.") == 7, "PDF finite assertion count")

print(json.dumps({"status": "PASS", "math_fidelity": fidelity,
                  "finite_premises": 7, "bibliography_entries": len(cites),
                  "unique_labels": len(labels), "build_diagnostics": 0,
                  "pdf_pages": text.count("\f"),
                  "scope": "editorial fidelity and build, not proof certification"},
                 sort_keys=True))
