# 02_file_io.py
import csv
import json

# Example CSV reading
with open('data/raw/sample.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

import pandas as pd

# Read CSV using pandas
df = pd.read_csv('data/raw/sample.csv')

# Simple transformation: total amount per category
summary = df.groupby('category')['amount'].sum().reset_index()

# Save transformed data
summary.to_csv('data/processed/summary.csv', index=False)

print("\nTransformed CSV saved to data/processed/summary.csv")
print(summary)        

# Example JSON reading
with open('data/raw/sample.json') as jsonfile:
    data = json.load(jsonfile)
    print(data)

# Read JSON using pandas
df_json = pd.read_json('data/raw/sample.json')

# Simple transformation: total amount per category
summary_json = df_json.groupby('category')['amount'].sum().reset_index()

# Save transformed JSON output
summary_json.to_csv('data/processed/summary_json.csv', index=False)

print("\nTransformed JSON saved to data/processed/summary_json.csv")
print(summary_json)
