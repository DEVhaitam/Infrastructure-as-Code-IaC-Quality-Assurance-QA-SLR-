#!/usr/bin/env python3
"""
remove_types.py

Removes BibTeX entries of certain types (e.g., @book, @proceedings)
and entries without a title field from an input .bib file.

Usage:
    python3 remove_types.py non-duplicate.bib filtered_nodup.bib
"""

import sys
import re

EXCLUDE_TYPES = {"book", "proceedings"}  # case-insensitive

def split_entries(bibtext):
    """
    Splits a .bib text into individual entries.
    Keeps comments or preamble text as separate blocks.
    """
    parts = re.split(r'(?=@\w+\s*\{)', bibtext, flags=re.MULTILINE)
    return [p for p in parts if p.strip() != ""]

def entry_type_and_key(entry):
    """
    Extracts the entry type and citation key.
    Returns (type, key) or (None, None) if parsing fails.
    """
    m = re.match(r'\s*@\s*([^{(]+)\s*[{(]\s*([^,]+)\s*,', entry, flags=re.IGNORECASE)
    if not m:
        return (None, None)
    return (m.group(1).strip().lower(), m.group(2).strip())

def has_title_field(entry):
    """
    Checks if the entry contains a title field.
    """
    # Search for something like title = { ... } or title = "..."
    return bool(re.search(r'\btitle\s*=\s*(\{[^}]+\}|"[^"]+")', entry, flags=re.IGNORECASE | re.S))

def remove_types_and_missing_titles(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        bibtext = f.read()

    entries = split_entries(bibtext)
    kept = []
    removed_type = 0
    removed_notitle = 0

    for e in entries:
        etype, key = entry_type_and_key(e)
        if etype is None:
            # keep non-standard text (comments, preamble)
            kept.append(e)
            continue

        # check type
        if etype.lower() in EXCLUDE_TYPES:
            removed_type += 1
            continue

        # check missing title
        if not has_title_field(e):
            removed_notitle += 1
            continue

        # keep valid entry
        kept.append(e)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("".join(kept))

    print(f"Processed {len(entries)} entries.")
    print(f"Removed {removed_type} entries of excluded types: {', '.join(EXCLUDE_TYPES)}")
    print(f"Removed {removed_notitle} entries without a title field.")
    print(f"Kept {len(kept)} entries. Written to {output_path}.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 remove_types.py input.bib output.bib")
        sys.exit(1)
    remove_types_and_missing_titles(sys.argv[1], sys.argv[2])
