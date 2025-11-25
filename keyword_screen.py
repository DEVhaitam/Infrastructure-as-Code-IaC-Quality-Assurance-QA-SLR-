#!/usr/bin/env python3
"""
keyword_screen.py

Performs keyword-based screening on a BibTeX file. Keeps entries only if they
contain at least one IaC keyword AND at least one quality keyword in any field.

Usage:
    python3 keyword_screen.py filtered_nodup.bib screened.bib included.csv excluded.csv

Outputs:
    screened.bib  - BibTeX with only included entries
    included.csv  - CSV listing included entries (key,title,matched_iac_terms,matched_quality_terms)
    excluded.csv  - CSV listing excluded entries (key,title,reason)
"""

import sys
import re
import csv

# === KEYWORDS ===
IAC_TERMS = [
    "infrastructure as code", "infrastructure-as-code", "iac", "configuration as code",
    "ansible", "terraform", "chef", "puppet", "pulumi", "docker", "dockerfile", "docker-compose",
    "docker compose", "docker-compose", "kubernetes", "k8s", "cloudformation", "cloud formation",
    "packer", "container", "containerization", "compose file", "ARM", "Juju", "Nomad", "TOSCA", "SaltStack", "CFEngine", "Heat"
]

QUALITY_TERMS = [
    "quality", "bug", "defect", "fault", "smell", "code smell", "anti-pattern", "antipattern",
    "antipattern", "vulnerability", "vulnerabilit", "security", "misconfiguration", "mis-config",
    "misconfig", "analysis", "analyzing", "testing", "test", "validation", "validate",
    "practice", "practice(s)", "lint", "linter", "linting", "performance", "reliability", "maintainability"
]

# compile normalized variants (lowercase)
IAC_TERMS = [t.lower() for t in IAC_TERMS]
QUALITY_TERMS = [t.lower() for t in QUALITY_TERMS]

# === helper functions ===
def split_entries(bibtext):
    parts = re.split(r'(?=@\w+\s*\{)', bibtext, flags=re.MULTILINE)
    return [p for p in parts if p.strip() != ""]

def entry_type_and_key(entry):
    m = re.match(r'\s*@\s*([^{(]+)\s*[{(]\s*([^,]+)\s*,', entry, flags=re.IGNORECASE)
    if not m:
        return (None, None)
    return (m.group(1).strip().lower(), m.group(2).strip())

def extract_fields(entry):
    """
    Extracts field names and values roughly. Returns dict of lowercased field contents concatenated.
    Not a full BibTeX parser, but good enough for title/abstract/keywords/note fields.
    """
    # remove leading @type{key,
    body = re.sub(r'^\s*@\w+\s*[{(]\s*[^,]+,', '', entry, count=1, flags=re.IGNORECASE | re.S)
    # remove trailing } or );
    body = re.sub(r'\}\s*$', '', body.strip(), flags=re.S)
    # find fields like fieldname = {value}  or field = "value"
    fields = {}
    for m in re.finditer(r'(\w+)\s*=\s*({(?P<br>[^}]*)}|\"(?P<qt>[^\"]*)\")\s*,?', body, flags=re.S):
        name = m.group(1).lower()
        val = (m.group('br') if m.group('br') is not None else m.group('qt') or "")
        fields[name] = val.strip()
    # also include entire body as fallback
    #fields['_all'] = " ".join(fields.values())
    return fields

def find_matches(text, terms):
    text = (text or "").lower()
    found = set()
    for t in terms:
        if t in text:
            found.add(t)
    return found

def screen_bib(input_path, out_bib, included_csv, excluded_csv):
    with open(input_path, 'r', encoding='utf-8') as f:
        bibtext = f.read()

    entries = split_entries(bibtext)
    included_entries = []
    excluded_rows = []
    included_rows = []
    SEARCH_FIELDS = ['title', 'abstract', 'keywords']

    for e in entries:
        etype, key = entry_type_and_key(e)
        if etype is None or key is None:
            # keep preamble / comments
            # treat as included to preserve file
            included_entries.append(e)
            continue

        fields = extract_fields(e)

        search_parts = []
        for field_name in SEARCH_FIELDS:
            # Get the value for the field, or an empty string if not present
            search_parts.append(fields.get(field_name, "")) 
            
        # 2. Combine only the selected fields into the text to be searched
        combined_text = " ".join(search_parts)

        #combined_text = " ".join(fields.values())
        iac_matches = find_matches(combined_text, IAC_TERMS)
        qual_matches = find_matches(combined_text, QUALITY_TERMS)

        if iac_matches and qual_matches:
            included_entries.append(e)
            title = fields.get('title', '')[:200].replace('\n', ' ')
            included_rows.append((key, title, ";".join(sorted(iac_matches)), ";".join(sorted(qual_matches))))
        else:
            title = fields.get('title', '')[:200].replace('\n', ' ')
            reasons = []
            if not iac_matches:
                reasons.append("no_IaC_term")
            if not qual_matches:
                reasons.append("no_quality_term")
            excluded_rows.append((key, title, ";".join(reasons)))

    # write included bib
    with open(out_bib, 'w', encoding='utf-8') as f:
        f.write("".join(included_entries))

    # write CSVs
    with open(included_csv, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['key','title','iac_matches','quality_matches'])
        for r in included_rows:
            w.writerow(r)

    with open(excluded_csv, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['key','title','reason'])
        for r in excluded_rows:
            w.writerow(r)

    print(f"Screening complete. {len(included_rows)} entries INCLUDED, {len(excluded_rows)} entries EXCLUDED.")
    print(f"Included bib written to: {out_bib}")
    print(f"Included CSV: {included_csv}")
    print(f"Excluded CSV: {excluded_csv}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 keyword_screen.py input_filtered.bib screened.bib included.csv excluded.csv")
        sys.exit(1)
    screen_bib(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
