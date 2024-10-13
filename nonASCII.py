import pandas as pd
import re

# Load your tweets CSV
df = pd.read_csv('/Users/wiktoria/Documents/master/Master thesis/August 31, 2014 - iCloud leak/August_24_2014_merged_links+apple+query+nick+dup.csv')

# Function to remove non-ASCII characters
def remove_non_ascii(text):
    return re.sub(r'[^\x00-\x7F]+', '', text)

# Apply the function to the 'Text' column
df['Text'] = df['Text'].apply(remove_non_ascii)

# Save the cleaned tweets to a new CSV
df.to_csv('cleaned_tweets.csv', index=False)

print("Non-ASCII characters removed successfully.")
