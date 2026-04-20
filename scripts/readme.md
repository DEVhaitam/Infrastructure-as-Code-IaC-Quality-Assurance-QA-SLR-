# Scripts Folder

This folder contains the Python scripts used in the replication package for the SLR. These scripts automate various steps in the data processing pipeline.

## Scripts Overview

### 1. `remove_types.py`
This script filters out irrelevant references from the `.bib` files. Specifically, it removes:
- Books
- Book chapters
- Entries with empty titles

#### Usage:
```bash
python remove_types.py ../data/processed_data/non-duplicate.bib ../data/processed_data/filtered_nodup.bib
```

### 2. `keyword_screen.py`
This script filters papers based on their title, abstract, and specific keywords related to IaC and quality assurance. It ensures that only relevant studies are retained for further analysis.

#### Usage:
```bash
python keyword_screen.py ../data/processed_data/input_filtered.bib ../data/processed_data/screened.bib ../data/processed_data/included.csv ../data/processed_data/excluded.csv
```
`input_filtered.bib`: is the file after removing irrelevant types and duplicates

`screened.bib`: is the file of retained papers

`included.csv`: is the file of retained papers with the lists of matching quality/iac terms

`excluded.csv`: is the file of excluded papers with the lists of missing quality/iac terms



### 3. `random_verification.py`
This script randomly selects 45 studies from the exclude.csv file for verification purposes.

#### Usage:
```bash
python random_verification.py
```
By default the script takes `../data/processed_data/excluded.csv` as input, and has `../data/processed_data/random_verification.csv` as output.
