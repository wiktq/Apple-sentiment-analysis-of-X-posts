import pandas as pd

# Load your CSV
csv_file = "/Users/wiktoria/Documents/master/Master thesis/August 31, 2014 - iCloud leak/August_24_2014_merged_links+apple+query.csv"  # Change to your actual path
df = pd.read_csv(csv_file)

# Function to check if 'apple' is only in the username
def filter_apple_in_username_only(row):
    text = row['Text'].lower()  # Make text lowercase for easier comparison
    # Check if 'apple' appears after '@' (username) and nowhere else in the tweet
    words_in_tweet = text.split()
    
    # Check if 'apple' is after '@' and not elsewhere in the tweet
    has_apple_username = any('@' in word and 'apple' in word for word in words_in_tweet)
    has_apple_elsewhere = 'apple' in text and not any('@' in word and 'apple' in word for word in words_in_tweet)
    
    # Keep tweet only if "apple" is mentioned outside the username or if the username is "@Apple"
    return not has_apple_username or has_apple_elsewhere or '@apple' in text

# Apply the filter
filtered_df = df[df.apply(filter_apple_in_username_only, axis=1)]

# Save the filtered tweets to a new CSV
filtered_df.to_csv("filtered_tweets.csv", index=False)

print(f"Filtered tweets saved to '/path/to/filtered_tweets.csv'")
