#!/usr/bin/env python3
"""
Term-frequency count over a BibTeX file.

Usage:
    python3 term_frequency.py                 # reads filtered_nodup.bib
    python3 term_frequency.py myfile.bib      # reads myfile.bib

Writes term_frequency.csv and prints the table.

Counts, for each term, the number of BibTeX entries whose title, abstract or
keywords mention it. An entry counts once per term, however many times the term
occurs in it.

Two counts are reported:
  raw      the term as written in the screening keyword list
  guarded  the same term restricted by a disambiguation context, for terms that
           are ambiguous outside the IaC domain (ARM = ARM processors, Heat =
           thermal, helm = nautical/idiomatic, cloud formation = meteorology,
           chef = culinary, packer = generic)
The gap between the two is the lexical ambiguity present in the candidate set.
"""

import csv
import re
import sys
from collections import Counter

DEFAULT_INPUT = "data/processed_data/filtered_nodup.bib"
OUTPUT = "data/processed_data/term_frequency.csv"

CM_CTX = (r"(configuration\s+management|playbook|cookbook|recipe|manifest|"
          r"provision|deployment|devops|infrastructure\s+as\s+code|\biac\b)")

# (group, name, raw patterns, unambiguous patterns, context required for raw)
GROUPS = [
    ("FOUNDATIONAL", "infrastructure as code", [r"infrastructure[\s\-]as[\s\-]code"], [], None),
    ("FOUNDATIONAL", "IaC", [r"\biac\b"], [], None),
    ("FOUNDATIONAL", "configuration as code", [r"configuration[\s\-]as[\s\-]code"], [], None),

    # compounds first: they mask their own text so "Docker Compose" is not also "Docker"
    ("TECHNOLOGY", "Docker Compose", [r"docker[\s\-_]?compose", r"compose\s+file"], [], None),
    ("TECHNOLOGY", "CloudFormation", [r"cloud[\s\-]?formation"],
     [r"cloudformation", r"aws\s+cloud\s?formation"],
     r"(\baws\b|amazon|template|stack|infrastructure\s+as\s+code|\biac\b)"),
    ("TECHNOLOGY", "Azure ARM", [r"\barm\b"],
     [r"arm\s+templates?", r"azure\s+resource\s+manager"],
     r"(azure|bicep|resource\s+manager)"),

    ("TECHNOLOGY", "Terraform", [r"terraform"], [], None),
    ("TECHNOLOGY", "Pulumi", [r"pulumi"], [], None),
    ("TECHNOLOGY", "Ansible", [r"ansible"], [], None),
    ("TECHNOLOGY", "Puppet", [r"puppet"], [], None),
    ("TECHNOLOGY", "Chef", [r"\bchef\b"], [], CM_CTX + r"|puppet|ansible|salt"),
    ("TECHNOLOGY", "SaltStack", [r"salt[\s\-_]?stack", r"\bsaltstack\b"], [], None),
    ("TECHNOLOGY", "CFEngine", [r"cf[\s\-_]?engine", r"\bcfengine\b"], [], None),
    ("TECHNOLOGY", "Docker", [r"docker", r"dockerfiles?"], [], None),
    ("TECHNOLOGY", "Packer", [r"\bpacker\b"], [r"hashicorp\s+packer"],
     r"(hashicorp|machine\s+image|vagrant|terraform|golden\s+image)"),
    ("TECHNOLOGY", "Kubernetes", [r"kubernetes", r"\bk8s\b"], [], None),
    ("TECHNOLOGY", "Helm", [r"\bhelm\b"], [r"helm\s+charts?"],
     r"(kubernetes|\bk8s\b|chart|cluster|cloud\s?native)"),
    ("TECHNOLOGY", "Nomad", [r"\bnomad\b"], [r"hashicorp\s+nomad"],
     r"(hashicorp|orchestrat|scheduler|cluster|workload)"),
    ("TECHNOLOGY", "Juju", [r"\bjuju\b"], [], None),
    ("TECHNOLOGY", "TOSCA", [r"\btosca\b"], [], None),
    ("TECHNOLOGY", "Heat", [r"\bheat\b"],
     [r"openstack\s+heat", r"heat\s+(templates?|orchestration)"],
     r"(openstack|orchestration\s+template)"),

    ("GENERIC", "container", [r"\bcontainers?\b"], [], None),
    ("GENERIC", "containerization", [r"containeri[sz]ation"], [], None),
]

FIELDS = ("title", "abstract", "keywords")


def read_entries(path):
    """Yield the concatenated title/abstract/keywords text of each BibTeX entry."""
    with open(path, encoding="utf-8", errors="replace") as handle:
        content = handle.read()

    chunks = re.split(r"@\w+\s*\{", content)[1:]   # split on @article{, @inproceedings{, ...
    for chunk in chunks:
        parts = []
        for field in FIELDS:
            m = re.search(rf"\b{field}\s*=\s*", chunk, re.IGNORECASE)
            if not m:
                continue
            i = m.end()
            while i < len(chunk) and chunk[i] in " \t\n":
                i += 1
            if i >= len(chunk):
                continue
            if chunk[i] == "{":                    # brace-delimited, may nest
                depth, j = 0, i
                while j < len(chunk):
                    if chunk[j] == "{":
                        depth += 1
                    elif chunk[j] == "}":
                        depth -= 1
                        if depth == 0:
                            break
                    j += 1
                parts.append(chunk[i + 1:j])
            elif chunk[i] == '"':                  # quote-delimited
                j = chunk.find('"', i + 1)
                parts.append(chunk[i + 1:j if j != -1 else len(chunk)])
            else:                                  # bare value
                j = chunk.find(",", i)
                parts.append(chunk[i:j if j != -1 else len(chunk)])
        text = re.sub(r"[{}\\]", " ", " ".join(parts))   # strip LaTeX braces/escapes
        yield re.sub(r"\s+", " ", text).strip().lower()


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_INPUT

    compiled = []
    for group, name, raws, stricts, ctx in GROUPS:
        compiled.append((
            group, name,
            re.compile(r"(?<![\w-])(?:" + "|".join(raws) + r")(?![\w-])", re.I),
            re.compile(r"(?<![\w-])(?:" + "|".join(stricts) + r")(?![\w-])", re.I) if stricts else None,
            re.compile(ctx, re.I) if ctx else None,
        ))

    raw_counts, guarded_counts = Counter(), Counter()
    tech_names = {n for g, n, *_ in GROUPS if g == "TECHNOLOGY"}
    total = no_tech_raw = no_tech_guarded = 0

    try:
        entries = list(read_entries(path))
    except FileNotFoundError:
        sys.exit(f"error: file not found: {path}")

    for text in entries:
        total += 1
        raw_hits, guarded_hits = set(), set()
        working = text
        for group, name, raw, strict, ctx in compiled:
            target = working if group == "TECHNOLOGY" else text
            strict_hit = bool(strict and strict.search(target))
            raw_hit = bool(raw.search(target))
            if raw_hit or strict_hit:
                raw_hits.add(name)
                if (strict is None and ctx is None) or strict_hit \
                        or (ctx is not None and ctx.search(text)):
                    guarded_hits.add(name)
            if group == "TECHNOLOGY" and raw_hit:
                working = raw.sub(" ", working)
        raw_counts.update(raw_hits)
        guarded_counts.update(guarded_hits)
        if not (raw_hits & tech_names):
            no_tech_raw += 1
        if not (guarded_hits & tech_names):
            no_tech_guarded += 1

    def pct(n):
        return f"{100 * n / total:.2f}" if total else "0.00"

    with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
        w = csv.writer(handle)
        w.writerow(["group", "term", "n_raw", "pct_raw", "n_guarded", "pct_guarded", "inflation"])
        for group, name, *_ in GROUPS:
            r, g = raw_counts.get(name, 0), guarded_counts.get(name, 0)
            w.writerow([group, name, r, pct(r), g, pct(g), r - g])
        w.writerow([])
        w.writerow(["", "TOTAL ENTRIES", total, "100.00", total, "100.00", 0])
        w.writerow(["", "NO TECHNOLOGY TERM", no_tech_raw, pct(no_tech_raw),
                    no_tech_guarded, pct(no_tech_guarded), no_tech_raw - no_tech_guarded])

    print(f"file    : {path}")
    print(f"entries : {total}")
    print(f"output  : {OUTPUT}\n")
    print(f"{'term':<26}{'raw':>8}{'guarded':>10}")
    for group, name, *_ in GROUPS:
        r, g = raw_counts.get(name, 0), guarded_counts.get(name, 0)
        if r:
            print(f"{name:<26}{r:>8}{g:>10}")
    print(f"\nno technology term: {no_tech_raw} raw / {no_tech_guarded} guarded "
          f"({pct(no_tech_guarded)}% of entries)")


if __name__ == "__main__":
    main()