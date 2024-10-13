import pandas as pd
import re

# Load your CSV file into a DataFrame
csv_file = "/Users/wiktoria/Documents/master/Master thesis/August 31, 2014 - iCloud leak/August_24_2014_merged.csv"  # Replace with your file path
df = pd.read_csv(csv_file)

# Function to remove URLs
def remove_links(text):
    return re.sub(r"http\S+", "", text)

# Apply the function to the 'Text' column of your DataFrame
df['Text'] = df['Text'].apply(remove_links)

# Save the cleaned tweets to a new CSV file
df.to_csv("cleaned_tweets.csv", index=False)

print("Links removed from tweets!")
