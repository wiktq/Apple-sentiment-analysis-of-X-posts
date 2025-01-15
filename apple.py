import pandas as pd

# Load your CSV file into a DataFrame
csv_file = "/path/to/your/file"  # Replace with your file path
df = pd.read_csv(csv_file)

# Filter rows where 'apple' is present in the tweet (case-insensitive)
df_filtered = df[df['Text'].str.contains("apple", case=False, na=False)]

# Save the filtered DataFrame to a new CSV file
df_filtered.to_csv("filtered_tweets.csv", index=False)

print("Tweets without 'apple' removed!")
