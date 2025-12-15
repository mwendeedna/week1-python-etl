import requests
import pandas as pd

# ----- Extract -----
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()
print("Sample data from API:")
print(data[:3])  # show first 3 records

# ----- Transform -----
df = pd.DataFrame(data)
summary = df.groupby("userId")["id"].count().reset_index()
summary.rename(columns={"id": "post_count"}, inplace=True)
print("\nPosts per user:")
print(summary)

# ----- Load -----
summary.to_csv("data/processed/api_posts_summary.csv", index=False)
print("\nSaved processed API data to data/processed/api_posts_summary.csv")
