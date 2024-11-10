import pandas as pd

# Load your Excel dataset
file_path = ''  # Replace with your actual file path
df = pd.read_excel(file_path)  # Use read_excel() for Excel files

# Set the number of random samples you want
sample_size = 1000

# Randomly sample 1000 rows without replacement
sampled_df = df.sample(n=sample_size, random_state=42)  # `random_state` for reproducibility

# Save the sample to a new CSV file
sampled_df.to_csv('random_1000_tweets.csv', index=False)

print(f"Random sample of {sample_size} tweets saved as csv file")
