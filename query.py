import pandas as pd

# Define the file path
csv_file = "/Users/wiktoria/Documents/master/Master thesis/August 24, 2011 - Steve Jobs resignation/August_24_2011_merged_links+apple.csv"  # Replace with your file path

# Load your CSV file into a DataFrame
df = pd.read_csv(csv_file)

# Define the lists of unwanted single words and exact phrases
unwanted_words = ["win", "free", "cinnamon", "caramel", "eat", "eating", "meal", "recipe", "dessert", 
                  "picking", "giveaway", "jack", "taste", "wood", "shabby", "slice", "bees", "banana", 
                  "ate", "cake", "viral", "sour", "flavor", "sauce", "peanut", "delicious", "pork", 
                  "tea", "crumble", "bread", "yummy", "seeds", "cherry", "hungry", "potato", "eatin", 
                  "eatinnnng", "chocolate", "watermelon"]

# List of exact phrases to match and remove
unwanted_phrases = ["big apple", "apples"]

# Remove rows with unwanted words
df_filtered = df[~df['Text'].str.contains('|'.join(unwanted_words), case=False, na=False)]

# Remove rows with unwanted exact phrases
for phrase in unwanted_phrases:
    df_filtered = df_filtered[~df_filtered['Text'].str.contains(r'\b' + phrase + r'\b', case=False, na=False)]

# Save the filtered DataFrame to a new CSV file
df_filtered.to_csv("filtered_tweets.csv", index=False)

print("Unwanted tweets removed and saved!")
