# file-cleaner
Takes in a CSV file and performs various data cleaning operations

## Features
- Remove duplicate rows

## Planned Features
- More specific duplicate removal
- Fill missing text fields with "Unknown"
- Strip whitespace from strings
- Output cleaned CSV file with a timestamped name

## Usage

- If input file is not given, will prompt user to select a file

```bash
python cleaner.py --input_file data/messy_data.csv --output_file data/cleaned_data.csv

