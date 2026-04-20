import csv
import random

# Input and output file names
input_file = '../data/processed_data/excluded.csv'
output_file = '../data/processed_data/random_verification.csv'

# Number of studies to select
num_studies = 45

# Read the data from the input file
with open(input_file, 'r', newline='', encoding='utf-8') as infile:
    reader = list(csv.reader(infile))
    header = reader[0]  # Extract the header
    rows = reader[1:]   # Extract the data rows

# Randomly select 45 rows
random_selection = random.sample(rows, num_studies)

# Write the selected rows to the output file
with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)  # Write the header
    writer.writerows(random_selection)  # Write the selected rows

print(f"Randomly selected {num_studies} studies written to {output_file}.")