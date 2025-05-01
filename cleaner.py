# src/cleaner.py
# refresher project to re-familiarize myself with python

import sys
import pandas as pd
import argparse
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

def clean_csv(input_file, output_file="blank"):
	df = pd.read_csv(input_file)

	print("Initial shape:", df.shape)
	print(df)

	####################
	# Strip whitespace #
	####################
	# Stripping first to make sure
	# duplicate rows are caught
	df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
	df.columns = df.columns.str.strip()
	print("Whitespace stripped")

	###################
	# Drop duplicates #
	###################
	# print("Would you like to drop duplicates (y/n)? ")
	# selection = input("Would you like to drop duplicates (y/n)? ")
	# while (selection == "y"):
	# 	print("Input the number with your preferred operation:")
	# 	print("1 - Remove duplicate rows")
	# 	print("2 - Remove rows with duplicates in a column")
	# 	selection = input()

	# 	if (selection == "1"):
	# 		# Drop rows with full duplicates across columns
	# 		df = df.drop_duplicates()
	# 	elif (selection == "2"):
	# 		# Offer choice of column
	# 		# Drop rows of matching column types
	# 		print("The columns available are:")
	# 		for name in df.columns:
	# 			print(name)
	# 		selection = input("Which would you like to drop duplicates from?")
	# 		df = df.drop_duplicates(selection)

	# 	selection = input("Do you have more duplicates to drop (y/n)? ")

	selection = input("Would you like to drop duplicate rows (y/n)? ")
	while (selection != "n" and selection != "y"):
		selection = input("Wrong. Would you like to drop duplicate rows (y/n)?")
	if (selection == "y"):
		df = df.drop_duplicates()
		print("Duplicate rows dropped")

	#######################
	# Fill missing values #
	#######################
	# Fill numbers with average (change this to something else?)
	# for col in df.select_dtypes(include=['float', 'int']).columns:
	# 	df[col].fillna(df[col].median())

	# Fill anything else with Unknown as a string
	for col in df.select_dtypes(include=['object']).columns:
		df[col] = df[col].fillna("Unknown")

	#####################
	# Save cleaned file #
	#####################
	# Mark new filename with time and save
	# if (output_file == "blank"):
	# 	timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
	# 	cleaned_filename = output_file or f"cleaned_{timestamp}.csv"
	# 	df.to_csv(cleaned_filename, index=False)

	# print(f"Cleaned data saved to {cleaned_filename}")

	print("New csv:")
	print(df)

if __name__ == "__main__":

	print(len(sys.argv))

	# Check for arguments
	# Use filedialog if nothing was passed via command line
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

		clean_csv(file_path)
