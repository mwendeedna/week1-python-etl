"""
Week 1 Practice Tasks
- Python Basics
- CSV & JSON File Handling
- Pandas Transformations
- API Ingestion
"""

# -------------------------------
# Part 1: Python Basics
# -------------------------------

# Task: FizzBuzz 1-10
# TODO: Implement FizzBuzz
print("=== Part 1: Python Basics ===")
for i in range(1, 11):  # numbers 1 to 10
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Quiz:
# 1. What does type(3.0) return?
# 2. Difference between '=' and '=='?

print(type(3.0))
print(5 == 5)

print("\n")  # Blank line to separate sections

# -------------------------------
# Part 2: CSV File Handling
# -------------------------------
print("=== Part 2: CSV File Handling ===")

# Task: Calculate average 'amount' per category from sample.csv
# Save result to: data/processed/average_per_category.csv
# TODO: Write code here

import pandas as pd

df = pd.read_csv('data/raw/sample.csv')
average_summary = df.groupby('category')['amount'].mean().reset_index()
average_summary.to_csv('data/processed/average_per_category.csv', index=False)

print("Average amount per category:")
print(average_summary)

# Quiz:
# 1. Difference between open('file.csv', 'r') and open('file.csv', 'w')?
# 2. What happens if you forget to close a file?
#Quiz Answers:
# 1. 'r' reads a file; 'w' writes and overwrites a file or creates it if missing.
# 2. Not closing a file can cause data loss, file locks, and memory issues.

print("\n")  # Blank line to separate sections

# -------------------------------
# Part 3: Pandas Transformations
# -------------------------------
print("=== Part 3: Pandas Transformations ===")

# Task:
# - Filter rows where amount > 150
# - Sort descending by amount
# - Save to data/processed/high_amount.csv
# TODO: Write code here

df = pd.read_csv("data/raw/sample.csv")

filtered_df = df[df['amount'] > 150]
filtered_df = filtered_df.sort_values(by='amount', ascending=False)

filtered_df.to_csv('data/processed/high_amount.csv', index=False)

print("Filtered & sorted data (amount > 150):")
print(filtered_df)
print("\nSaved to data/processed/high_amount.csv")


# Quiz:
# 1. What does df.head() do?
# 2. How to reset index after filtering?

Quiz Answers:
# 1. df.head() displays the first 5 rows of a DataFrame for inspection.
# 2. Use df.reset_index(drop=True) to reset the index after filtering.
print("\n")  # Blank line to separate sections

# -------------------------------
# Part 4: JSON File Handling
# -------------------------------
print("=== Part 4: JSON File Handling ===")

# Task:
# - Read sample.json
# - Add new column 'amount_doubled' = amount * 2
# - Save to data/processed/sample_json_doubled.csv
# TODO: Write code here

import json
import pandas as pd

# Load JSON file
with open("data/raw/sample.json", "r") as file:
    json_data = json.load(file)

print("Raw JSON data:")
print(json_data)

# Convert JSON to DataFrame
df_json = pd.DataFrame(json_data)

# Simple transformation: total amount per category
json_summary = (
    df_json
    .groupby("category")["amount"]
    .sum()
    .reset_index()
)

# Save output
output_path = "data/processed/json_summary.csv"
json_summary.to_csv(output_path, index=False)

print("\nJSON summary saved to:", output_path)
print(json_summary)


print("\n")  # Blank line to separate sections

# -------------------------------
# Part 5: API Ingestion
# -------------------------------
print("=== Part 5: API Ingestion ===")

# Task:
# - Fetch posts from https://jsonplaceholder.typicode.com/posts
# - Count posts where title contains "eum"
# - Print that count
# TODO: Write code here

# 06_api_ingestion.py
import requests
import pandas as pd

# Public API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# Make API request
response = requests.get(url)

# Validate response
print("Status Code:", response.status_code)

if response.status_code != 200:
    raise Exception("API request failed")

# Parse JSON
data = response.json()

# Convert to DataFrame
df = pd.DataFrame(data)

# Basic transformation: select useful columns
df = df[["userId", "id", "title"]]

# Save output
output_path = "data/processed/api_posts.csv"
df.to_csv(output_path, index=False)

print(f"API data saved to {output_path}")
print(df.head())


# Quiz:
# 1. What Python module is used to send HTTP requests?
# 2. What does response.json() return?

# Quiz Answers:
# 1. The requests module is used to send HTTP requests.
# 2. response.json() returns the API response as a Python object (dict or list).