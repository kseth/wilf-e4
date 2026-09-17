"""Editorial TeX/PRELIM fidelity and build audit, not a proof checker.

Run after `make pdf` in manuscript/. Requires Poppler's pdftotext.
The proof spine and analytic mathematics are compared. Implementation
arithmetic envelopes remain in PRELIM rather than the revised manuscript.
Approved rewritten mathematics has explicit regression snapshots below.
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


def replace_span(source, start, end, replacement):
    require(source.count(start) == 1 and source.count(end) == 1,
            "approved rewrite boundaries are missing or ambiguous")
    left, right = source.index(start), source.index(end)
    require(left < right, "approved rewrite boundaries are reversed")
    return source[:left] + replacement + source[right:]


def replace_once(source, old, new):
    require(source.count(old) == 1, "approved formula rewrite missing or repeated")
    return source.replace(old, new)


# A common cutoff lemma replaces three branch-specific quadratic arguments.
# Its assumptions and the exact three parameter pairs are regression checked.
CUTOFF_MATH = r"""
\(H>3\) \(D_0<m\)
\[
\frac{D_0}{m}\ge\alpha H-\beta B,\qquad
\alpha>0,\quad 0\le\beta\le3.
\]
\[\boxed{H<C:=3+\frac{1+9\beta}{\alpha}}.\]
\(\alpha H<1+\beta B\) \(H-3\)
\[
\alpha H^2-(3\alpha+1+9\beta)H+3-\beta
=\alpha H(H-C)+3-\beta<0.
\]
\(H\ge C\) \(\alpha>0\) \(3-\beta\ge0\)
\(\alpha\) \(\beta\)
\(1/3\) \(2/3\) \(H<24\)
\(1/3\) \(4/3\) \(H<42\)
\(5/42\) \(37/42\) \(H<78\)
"""


# These formulas replace only Appendix B.4--B.5's repeated definitions and
# parallel calculations. The six-column obstruction remains source-matched.
PROJECTION_MATH = r"""
\(\Phi(T,K)\ge0\) \(K=\operatorname{Max}(T)\)
\(Q=Q_k\) \(k\in\{3,4\}\) \(\Phi(T,K)\ge0\)
\(\alpha\) \(b,d>a\)
\(Q_3\) \(\alpha,\beta,\gamma\) \(\alpha>\beta,\gamma\ge1\)
\(Q_4\) \(\alpha,\beta,\gamma,\delta\)
\(\alpha>\beta>\gamma\ge1,\ \alpha>\delta\ge1\)
\(\alpha\ge k-1\) \(K\)
\[|K|=k,\qquad P(T)=k+\alpha+m.\]
\(2k-4\) \(k-1\)
\[
\sum_{x\in K}|x|_1=m+k-4,\qquad
\sum_j\max_{x\in K}x_j=\alpha+k-2.
\]
\[
E(K)=m-\alpha-2,\qquad
\Phi(T,K)=2(\alpha-k+1)\ge0.
\]
\(x\) \(\Phi(T,K)\ge0\) \(W_4(S)\ge0\)
"""


spine = (ROOT / "prelim/proof.md").read_text(encoding="utf-8")
spine = spine[spine.index("## 1. "):
              spine.index("All finite predicates are exact integer comparisons.")]
spine = re.sub(r"^> ?", "", spine, flags=re.M)
# The interval and strip displays now cite the one recurrence in Appendix A.
spine = without_tagged_displays(spine, {"14", "23"})
spine = replace_once(spine,
                     "## 5. Structural geometry and a reusable exact interval method",
                     CUTOFF_MATH + "\n## 5. Structural geometry and a reusable exact interval method")
spine = replace_once(spine, r"""\[
H<3+2B,\qquad H^2-24H+7<0,\qquad H<24.
\]""", r"\(H<24\)")
spine = replace_once(spine,
                     r"\(H<3+4B\), hence \(H^2-42H+5<0\) and \(H<42\).",
                     r"\(H<42\).")
spine = replace_once(spine, r"\(5H^2-390H+89<0\)", "")
analytic = (ROOT / "prelim/analytic-details.md").read_text(encoding="utf-8")
b = analytic.index("## Appendix B:")
c = analytic.index("## Appendix C:")
# The only mathematical notation change in the import is local w(x) -> lambda(x).
analytic = analytic[:b] + analytic[b:c].replace("w(", r"\lambda(") + analytic[c:]
analytic = replace_span(analytic, "### B.4. The remaining projection scores",
                        "## Appendix C:", PROJECTION_MATH)

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
        if expected != actual:
            first = next((i for i, pair in enumerate(zip(expected, actual))
                          if pair[0] != pair[1]), min(len(expected), len(actual)))
            require(False, f"{name} {kind} differ at expression {first}: "
                    f"expected {expected[first:first+1]}, got {actual[first:first+1]}")
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
