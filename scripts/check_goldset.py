"""
check_goldset.py — checks how many of the 25 quasi-goldset papers are
present in a given BibTeX file.

Usage:
    python check_goldset.py <input.bib>
"""

import sys
import os
import re

# ── 25 quasi-goldset papers (id, title, year) ────────────────────────────────
GOLDSET = [
    # From close related surveys (16)
    (1,  "The seven sins: security smells in infrastructure as code scripts",                             2019),
    (2,  "Does your configuration code smell?",                                                          2016),
    (3,  "Security smells in ansible and chef scripts: a replication study",                             2021),
    (4,  "Within-project defect prediction of infrastructure-as-code using product and process metrics", 2021),
    (5,  "Rehearsal: a configuration verification tool for puppet",                                      2016),
    (6,  "Code smells in infrastructure as code",                                                        2018),
    (7,  "Gang of eight: a defect taxonomy for infrastructure as code scripts",                          2020),
    (8,  "Characterizing defective configuration scripts used for continuous deployment",                 2018),
    (9,  "Source code properties of defective infrastructure as code scripts",                           2019),
    (10, "Glitch: automated polyglot security smell detection in infrastructure as code",                 2022),
    (11, "Towards semantic detection of smells in cloud infrastructure code",                            2020),
    (12, "Analyzing infrastructure as code to prevent intra-update sniping vulnerabilities",             2021),
    (13, "DeepIaC: deep learning-based linguistic anti-pattern detection in IaC",                        2020),
    (14, "Automatically detecting risky scripts in infrastructure code",                                 2020),
    (15, "As code testing: characterizing test quality in open source ansible development",              2022),
    (16, "Sommelier: a tool for validating TOSCA application topologies",                                2017),
    # From academic IaC expertise (9)
    (17, "Security misconfigurations in open source kubernetes manifests: an empirical study",           2023),
    (18, "Co-evolution of infrastructure and source code: an empirical study",                           2015),
    (19, "Toward a catalog of software quality metrics for infrastructure code",                         2020),
    (20, "How good is your puppet? an empirically defined and validated quality model for puppet",       2018),
    (21, "Control and data flow in security smell detection for infrastructure as code: is it worth the effort?", 2023),
    (22, "Smelly variables in ansible infrastructure code: detection, prevalence, and lifetime",         2022),
    (23, "Automated infrastructure as code program testing",                                             2024),
    (24, "Infrastructure as code for dynamic deployments",                                               2022),
    (25, "Characteristics of defective infrastructure as code scripts in devops",                       2018),
]

STOP = {
    "a", "an", "the", "in", "of", "and", "or", "for", "to", "as", "on",
    "at", "by", "with", "is", "are", "was", "were", "it", "its", "this",
    "that", "from", "into", "your", "our", "their", "does", "do",
}


def tokenize(title: str) -> set:
    t = title.lower()
    t = re.sub(r"[^\w\s]", " ", t)
    return {w for w in t.split() if w not in STOP and len(w) > 1}


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def extract_bib_entries(content: str) -> list:
    """Return list of {'key': str, 'title': str} for every entry in the bib file."""

    # Title field: outer braces with up to two levels of nesting inside
    title_re = re.compile(
        r"\btitle\s*=\s*\{((?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*)\}",
        re.IGNORECASE | re.DOTALL,
    )
    key_re = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,", re.IGNORECASE)

    keys   = [(m.start(), m.group(1).strip()) for m in key_re.finditer(content)]
    titles = [
        (m.start(), re.sub(r"[{}]", "", m.group(1)).strip())
        for m in title_re.finditer(content)
    ]

    entries = []
    for t_pos, t_text in titles:
        preceding = [(kp, ks) for kp, ks in keys if kp < t_pos]
        if preceding:
            _, key = max(preceding, key=lambda x: x[0])
            entries.append({"key": key, "title": t_text})

    return entries


def best_match(gold_title: str, bib_entries: list, threshold: float = 0.50):
    """Return (entry, score) for the best match, or (None, score) if below threshold."""
    gold_tok = tokenize(gold_title)
    best_score, best_entry = 0.0, None

    for entry in bib_entries:
        score = jaccard(gold_tok, tokenize(entry["title"]))
        if score > best_score:
            best_score, best_entry = score, entry

    if best_score >= threshold:
        return best_entry, best_score
    return None, best_score


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {os.path.basename(sys.argv[0])} <input.bib>")
        sys.exit(1)

    bib_path = sys.argv[1]
    if not os.path.isfile(bib_path):
        print(f"Error: file not found: {bib_path}")
        sys.exit(1)

    with open(bib_path, encoding="utf-8") as f:
        content = f.read()

    entries = extract_bib_entries(content)

    found, missed = [], []
    for gid, gtitle, gyear in GOLDSET:
        entry, score = best_match(gtitle, entries)
        if entry:
            found.append((gid, gtitle, gyear, entry, score))
        else:
            missed.append((gid, gtitle, gyear))

    SEP  = "=" * 72
    TITLE_W = 62

    print(f"\n{SEP}")
    print(f"  Quasi-Goldset Coverage Check")
    print(f"  File   : {bib_path}")
    print(f"  Entries: {len(entries)}")
    print(SEP)
    print(f"\n  Score: {len(found)} / {len(GOLDSET)}\n")

    print(f"  FOUND ({len(found)}):")
    for gid, gtitle, gyear, entry, score in found:
        label = f"[{gid:2d}] {gtitle[:TITLE_W]}"
        print(f"    {label:<{TITLE_W + 5}}  → {entry['key']}  ({score:.2f})")

    print(f"\n  MISSED ({len(missed)}):")
    for gid, gtitle, gyear in missed:
        year_s = f" ({gyear})" if gyear else ""
        print(f"    [{gid:2d}] {gtitle}{year_s}")

    print()


if __name__ == "__main__":
    main()
