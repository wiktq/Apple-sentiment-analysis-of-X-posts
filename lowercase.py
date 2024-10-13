import pandas as pd

# Load your CSV file with tweets
df = pd.read_csv('/path/to/file/')

# Convert the 'Text' column (or your equivalent tweet text column) to lowercase
df['Text'] = df['Text'].str.lower()

# Save the modified dataframe to a new CSV file
df.to_csv('lowercase_tweets.csv', index=False)

print("All tweets have been converted to lowercase.")
