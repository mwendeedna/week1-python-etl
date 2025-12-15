import csv
import json
import pandas as pd

# ----- CSV Processing -----
print("CSV Data:")
with open('data/raw/sample.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

df = pd.read_csv('data/raw/sample.csv')
summary = df.groupby('category')['amount'].sum().reset_index()
summary.to_csv('data/processed/summary.csv', index=False)
print("\nTransformed CSV saved to data/processed/summary.csv")
print(summary)

# ----- JSON Processing -----
print("\nJSON Data:")
with open('data/raw/sample.json') as jsonfile:
    data = json.load(jsonfile)
    print(data)

df_json = pd.read_json('data/raw/sample.json')
summary_json = df_json.groupby('category')['amount'].sum().reset_index()
summary_json.to_csv('data/processed/summary_json.csv', index=False)
print("\nTransformed JSON saved to data/processed/summary_json.csv")
print(summary_json)

