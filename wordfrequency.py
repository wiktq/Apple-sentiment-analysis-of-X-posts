import pandas as pd
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords

# If you don't have stopwords downloaded, uncomment this line and run it once
nltk.download('stopwords')

# Load CSV
csv_file = "/Users/wiktoria/Documents/master/Master thesis/All tweets"  # Replace with your file path
df = pd.read_csv(csv_file)

# Define stopwords
stop_words = set(stopwords.words('english'))

# Function to clean and tokenize tweets
def clean_tokenize_tweets(text):
    # Remove special characters and numbers
    text = re.sub(r'[^A-Za-z\s]', '', text)
    # Tokenize and lowercase
    words = text.lower().split()
    # Remove stopwords
    words = [word for word in words if word not in stop_words]
    return words

# Combine all tweets into one long text
all_tweets = " ".join(df['Text'].astype(str))

# Clean and tokenize
tokens = clean_tokenize_tweets(all_tweets)

# Count word frequencies
word_freq = Counter(tokens)

# Display the most common words
most_common_words = word_freq.most_common(50)  # Top 50 words
print(most_common_words)

# Save frequency to CSV for easy review
freq_df = pd.DataFrame(most_common_words, columns=['Word', 'Frequency'])
freq_df.to_csv("word_frequencies.csv", index=False)
