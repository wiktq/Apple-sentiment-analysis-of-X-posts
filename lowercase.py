import pandas as pd

# Load your CSV file with tweets
df = pd.read_csv('/Users/wiktoria/Documents/master/Master thesis/August 31, 2014 - iCloud leak/August_24_2014_merged_links+apple+query+nick+dup+ASCII.csv')

# Convert the 'Text' column (or your equivalent tweet text column) to lowercase
df['Text'] = df['Text'].str.lower()

# Save the modified dataframe to a new CSV file
df.to_csv('lowercase_tweets.csv', index=False)

print("All tweets have been converted to lowercase.")
