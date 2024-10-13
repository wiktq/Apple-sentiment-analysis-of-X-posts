import pandas as pd
import re

# Load your tweets CSV
df = pd.read_csv('/path/to/file/')

# Function to remove non-ASCII characters
def remove_non_ascii(text):
    return re.sub(r'[^\x00-\x7F]+', '', text)

# Apply the function to the 'Text' column
df['Text'] = df['Text'].apply(remove_non_ascii)

# Save the cleaned tweets to a new CSV
df.to_csv('cleaned_tweets.csv', index=False)

print("Non-ASCII characters removed successfully.")
