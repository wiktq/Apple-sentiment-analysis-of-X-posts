import pandas as pd

# Load your full dataset
file_path = '/Users/wiktoria/Documents/master/Master thesis/All tweets/ALL TWEETS sentiment_per_tweet.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Filter the dataset to include only rows where Column K is 1 or -1
filtered_df = df[df['K'].isin([1, -1])]  # Column 'K' should be where your sentiment labels (1 or -1) are

# Set the number of random samples you want
sample_size = 1000

# Randomly sample 1000 tweets without replacement from the filtered data
sampled_df = filtered_df.sample(n=sample_size, random_state=42)  # `random_state` for reproducibility

# Save the sample to a new CSV file
sampled_df.to_csv('random_1000_filtered_tweets.csv', index=False)

print(f"Random sample of {sample_size} tweets with sentiment 1 or -1 saved as csv file")

