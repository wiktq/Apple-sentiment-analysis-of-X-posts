import os
import pandas as pd
from collections import Counter
import nltk
from nltk.corpus import stopwords
import string

# Download NLTK stopwords
nltk.download('stopwords')

# Define the CSV file or directory path
csv_file = '/path/to/your/excel'  # Change to your file path

# Load the CSV file
df = pd.read_csv(csv_file)

# Get the tweet text column
tweets = df['Text']  # Assuming your CSV has a 'Text' column with tweets

# Combine all tweets into one text
all_text = ' '.join(tweets)

# Remove punctuation and convert to lowercase
translator = str.maketrans('', '', string.punctuation)
all_text = all_text.translate(translator).lower()

# Split text into words
words = all_text.split()

# Remove stopwords
filtered_words = [word for word in words if word not in stopwords.words('english')]

# Calculate word frequencies
word_freq = Counter(filtered_words)

# Convert the word frequency dictionary to a DataFrame
word_freq_df = pd.DataFrame(word_freq.items(), columns=['Word', 'Frequency'])

# Sort by frequency
word_freq_df = word_freq_df.sort_values(by='Frequency', ascending=False)

# Save to CSV
output_file = '/path/to/second/csv/'  # Change to your output file path
word_freq_df.to_csv(output_file, index=False)

print(f"Word frequency analysis saved to {output_file}")
