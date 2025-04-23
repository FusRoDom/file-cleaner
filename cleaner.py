# src/cleaner.py
# refresher project to re-familiarize myself with python

import sys
import pandas as pd
import argparse
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

def clean_csv(input_file, output_file):
	df = pd.read_csv(input_file)

	print("Initial shape:", df.shape)
	print(df.head())

	# Drop duplicates
	df = df.drop_duplicates()

	# Strip whitespace from strings
	# df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
	# df.columns = df.columns.str.strip()

	# Fill missing values
	# for col in df.select_dtypes(include=['float', 'int']).columns:
	# 	df[col].fillna(df[col].median(), inplace=True)

	# for col in df.select_dtypes(include=['object']).columns:
	# 	df[col].fillna("Unknown", inplace=True)

	# Save cleaned file
	# timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
	# cleaned_filename = output_file or f"cleaned_{timestamp}.csv"
	# df.to_csv(cleaned_filename, index=False)

	# print(f"Cleaned data saved to {cleaned_filename}")
	print(df.head())

#def print_csv(clean_file):
	

if __name__ == "__main__":

	print(len(sys.argv))

	if (len(sys.argv) > 1):		
		#parse arguments
		parser = argparse.ArgumentParser(description="Clean a CSV file")
		parser.add_argument("input_file", help="Path to the input CSV")
		parser.add_argument("--output_file", help="Optional output file name")

		args = parser.parse_args()

		clean_csv(args.input_file, args.output_file)
	else:
		# tkinter initialization
		root = tk.Tk()
		root.withdraw()

		file_path = filedialog.askopenfilename()

		clean_csv(file_path, file_path)