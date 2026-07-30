"""
check_goldset.py — checks how many of the 52 quasi-goldset papers are
present in a given BibTeX file.

Usage:
    python check_goldset.py <input.bib>
"""

import sys
import os
import re

# ── 53 quasi-goldset papers (id, title, year) ────────────────────────────────
# Built from goldset/qgs_zhang.md
GOLDSET = [
    # From MSR (10)
    (1,  "Co-evolution of infrastructure and source code: an empirical study",                           2015),
    (2,  "Does your configuration code smell?",                                                          2016),
    (3,  "An empirical analysis of the docker container ecosystem on GitHub",                            2017),
    (4,  "Smelly variables in ansible infrastructure code: detection, prevalence, and lifetime",         2022),
    (5,  "Control and data flow in security smell detection for infrastructure as code: is it worth the effort?", 2023),
    (6,  "Fine-grained just-in-time defect prediction at the block level in infrastructure-as-code (IaC)", 2024),
    (7,  "DRMiner: a tool for identifying and analyzing refactorings in Dockerfile",                     2024),
    (8,  "Smells-sus: sustainability smells in IaC",                                                     2025),
    (9,  "It works (only) on my machine: a study on reproducibility smells in ansible scripts",          2025),
    (10, "Refactoring for Dockerfile quality: a dive into developer practices and automation potential", 2025),
    # From ICSE (5)
    (11, "The seven sins: security smells in infrastructure as code scripts",                            2019),
    (12, "Gang of eight: a defect taxonomy for infrastructure as code scripts",                          2020),
    (13, "Practical fault detection in puppet programs",                                                 2020),
    (14, "Shipwright: a human-in-the-loop system for Dockerfile repair",                                 2021),
    (15, "Empirical study of the docker smells impact on the image size",                                2024),
    # From ASE (4)
    (16, "Tortoise: interactive system configuration repair",                                            2017),
    (17, "Polyglot code smell detection for infrastructure as code with GLITCH",                         2023),
    (18, "Leveraging practitioners' feedback to improve a security linter",                               2023),
    (19, "Ansible Lightspeed: a code generation service for IT automation",                               2024),
    # From FSE (2)
    (20, "Infrastructure as code for dynamic deployments",                                                2022),
    (21, "State reconciliation defects in infrastructure as code",                                        2024),
    # From ICST (3)
    (22, "Characterizing defective configuration scripts used for continuous deployment",                2018),
    (23, "As code testing: characterizing test quality in open source ansible development",              2022),
    (24, "Smoke testing of cloud systems",                                                                2022),
    # From SANER (3)
    (25, "How good is your puppet? an empirically defined and validated quality model for puppet",       2018),
    (26, "Lessons from research to practice on writing better quality puppet scripts",                   2022),
    (27, "On the prevalence, co-occurrence, and impact of infrastructure-as-code smells",                 2024),
    # From ICSME (3)
    (28, "Assessing and improving the quality of docker artifacts",                                       2022),
    (29, "Defuse: a data annotator and model builder for software defect prediction",                     2022),
    (30, "DockerCleaner: automatic repair of security smells in Dockerfiles",                             2023),
    # From ISSTA (3)
    (31, "An empirical study on Kubernetes operator bugs",                                                2024),
    (32, "InfraFix: technology-agnostic repair of infrastructure as code",                                2025),
    (33, "Hybrid fuzzing of infrastructure as code programs",                                             2025),
    # From TSE (3)
    (34, "Within-project defect prediction of infrastructure-as-code using product and process metrics", 2022),
    (35, "Detecting and characterizing propagation of security weaknesses in puppet-based infrastructure management", 2023),
    (36, "Automated infrastructure as code program testing",                                              2024),
    # From TOSEM (4)
    (37, "Security smells in ansible and chef scripts: a replication study",                              2021),
    (38, "Security misconfigurations in open source kubernetes manifests: an empirical study",            2023),
    (39, "DRIVE: Dockerfile rule mining and violation detection",                                         2023),
    (40, "On the understandability of design-level security practices in infrastructure-as-code scripts and deployment architectures", 2024),
    # From EMSE (7)
    (41, "The \"as code\" activities: development anti-patterns for infrastructure as code",              2020),
    (42, "FindICI: using machine learning to detect linguistic inconsistencies between code and natural language descriptions in infrastructure-as-code", 2022),
    (43, "An empirical study of task infections in ansible scripts",                                      2023),
    (44, "Patterns of multi-container composition for service orchestration with docker compose",         2024),
    (45, "Assessing the adoption of security policies by developers in terraform across different cloud providers", 2025),
    (46, "Analyzing and mitigating (with LLMs) the security misconfigurations of helm charts from artifact hub", 2025),
    (47, "Vulnerabilities in infrastructure as code: what, how many, and who?",                           2025),
    # From JSS (2)
    (48, "Toward a catalog of software quality metrics for infrastructure code",                          2020),
    (49, "On the practice of semantic versioning for ansible galaxy roles: an empirical study and a change classification model", 2021),
    #From SoCC (1)
    (50, "Automatically detecting risky scripts in infrastructure code",                                  2020),
    # From past SLRs (3)
    (51, "Code smells in infrastructure as code",                                                         2018),
    (52, "DeepIaC: deep learning-based linguistic anti-pattern detection in IaC",                         2020),
    (53, "Sommelier: a tool for validating TOSCA application topologies",                                 2017),
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
