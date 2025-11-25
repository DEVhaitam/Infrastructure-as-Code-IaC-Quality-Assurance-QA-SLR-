# Replication Package for Systematic Literature Review (SLR) on Infrastructure as Code (IaC)

This repository contains the replication package for our Systematic Literature Review (SLR) on Infrastructure as Code (IaC) Quality Assurance (QA). The package includes all the files and scripts necessary to reproduce the results of our study.

## Repository Structure

The following files are included in this replication package:

1. **`all.bib`**  
    This file contains the results of our initial search query.

2. **`non-duplicate.bib`**  
    This file contains the results of the `all.bib` file after removing duplicates using [Parsifal](https://parsif.al/).

3. **`filtered_nondup.bib`**  
    This file contains the results of the `remove_types.py` script, which filters out irrelevant references such as books, book chapters, and entries with empty titles.

4. **`screened.bib`**  
    This file contains the results of the `keyword_screen.py` script, which filters papers based on title, abstract, IaC-related terms, and quality-related terms.

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

## Scripts

- **`remove_types.py`**  
  A Python script to remove irrelevant references such as books, book chapters, and entries with empty titles.

- **`keyword_screen.py`**  
  A Python script to filter papers based on title, abstract, and specific keywords related to IaC and quality.

## Reproducibility

To reproduce the results, follow the steps outlined above using the provided `.bib` files and scripts. Ensure that you have Python installed to run the scripts.

## Contact

For any questions or issues regarding this replication package, please contact the authors.
