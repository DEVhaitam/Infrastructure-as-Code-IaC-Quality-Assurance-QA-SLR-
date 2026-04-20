# Replication Package for Systematic Literature Review (SLR) on Infrastructure as Code (IaC)

This repository contains the replication package for our Systematic Literature Review (SLR) on Infrastructure as Code (IaC) Quality Assurance (QA). The package includes all the files and scripts necessary to reproduce the results of our study.

## Repository Structure

The following folders are included in this replication package:

1. **`scripts/`**  
    This folder contains Python scripts used for data processing:
    - `remove_types.py`: Removes irrelevant references such as books, book chapters, and entries with empty titles.
    - `keyword_screen.py`: Filters papers based on title, abstract, and specific keywords related to IaC and quality.
    - `random_selection.py`: Randomly selects 45 studies out of the excluded papers.

2. **`data/`**  
    This folder contains raw and processed data files:
    - `raw_data/`: Contains the raw data file, `all.bib`, retrieved through applying the search query.
    - `processed_data/`: Contains intermediate and processed data files, such as `non-duplicate.bib`, `filtered_nondup.bib`, and `screened.bib`.
    - `results/`: Contains the main spreadsheet presenting the final results of the study.

## Process Overview

The following steps outline the process used to produce the results:

1. **Search Query**  
    The initial search query was conducted, and the results were saved in `all.bib`.

2. **Duplicate Removal**  
    Duplicates were removed from `all.bib` using Parsifal, resulting in `non-duplicate.bib`.

3. **Filtering Irrelevant References**  
    The `remove_types.py` script was used to filter out irrelevant references, producing `filtered_nondup.bib`.

4. **Keyword Screening**  
    The `keyword_screen.py` script was applied to filter papers based on title, abstract, and relevant terms, resulting in `screened.bib`.

## Reproducibility

To reproduce the results, follow the steps outlined above using the provided `.bib` files and scripts. Ensure that you have Python installed to run the scripts.

## Contact

For any questions or issues regarding this replication package, please contact the authors.
