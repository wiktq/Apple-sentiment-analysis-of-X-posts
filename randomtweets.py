import pandas as pd

# Load your full dataset
file_path = '/Users/wiktoria/Desktop/Book1.xlsx'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Set the number of random samples you want
sample_size = 1000

# Randomly sample 1000 tweets without replacement
sampled_df = df.sample(n=sample_size, random_state=42)  # `random_state` for reproducibility

# Save the sample to a new CSV file
sampled_df.to_csv('random 1000 tweets.csv', index=False)

print(f"Random sample of {sample_size} tweets saved as csv file")
