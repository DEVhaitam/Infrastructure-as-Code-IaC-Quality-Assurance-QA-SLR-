# Data Folder

This folder contains the data files used and generated during the replication package for the SLR. The files in this folder include raw data, intermediate results, and final processed data.

## Folder Structure

### 1. `raw_data/`
This subfolder contains the raw data collected during the initial stage of the study. This folder includes:
- `all.bib`: The complete set of references retrieved from the search query.


### 2. `processed_data/`
This subfolder contains the processed data files generated after applying the scripts. These files include:
- `non-duplicate.bib`: The `.bib` file after removing duplicate entries.
- `filtered_nondup.bib`: The `.bib` file after filtering irrelevant references.
- `screened.bib`: The `.bib` file after keyword screening.
- `included.csv`: A CSV file listing studies included during the screening process, with columns:
  - `key`: Unique identifier for the study.
  - `title`: Title of the study.
  - `iac_matches`: Matched IaC terms.
  - `quality_matches`: Matched Quality terms.
- `excluded.csv`: A CSV file listing studies excluded during the screening process, with columns:
  - `key`: Unique identifier for the study.
  - `title`: Title of the study.
  - `reason`: Reason for exclusion.
- `random_verification.csv`: A CSV file containing the random 45 selected studies for verification.


### 3. `results/`
This subfolder contains the final spreadsheet we used for analyzing our results, with the following sheets included:
- `Final set of papers`: Contains the final set of the 70 studies with their classifications across the different dimensions.
- `Kappa`: Contains the differences between authores' responses, and how the kappa coefficient was calculated.
- `IaC_issues_across_platforms`: Contains a table with the distribution of quality issues across the IaC technologies.
- `IaC_issues_across_layers`: Contains a table with the distribution of quality issues across IaC layers.
- `Exploratory phase`: Contains a table with the results of the exokiratory during the design of the search query.
- `Visualizations`: Contains statistics and visualizations about the papers.