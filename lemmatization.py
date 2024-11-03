import pandas as pd
import re
import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data if not already downloaded
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Function to convert POS tags for lemmatizer
def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ, "N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

# Load the dataset
file_path = '/Users/wiktoria/Documents/master/Master thesis/March 5, 2010/March_5_2010_merged_links+apple+query+nick+dup+ASCII+lowercase+stopwords.csv'  # Replace with your actual path
df = pd.read_csv(file_path)

# Function for lemmatizing each word in a tweet
def lemmatize_text(text):
    words = nltk.word_tokenize(text)
    lemmatized_words = [lemmatizer.lemmatize(word, get_wordnet_pos(word)) for word in words]
    return ' '.join(lemmatized_words)

# Remove mentions except "@Apple" and lemmatize the text
def clean_and_lemmatize_text(text):
    # Remove mentions except @Apple
    text = re.sub(r'@\b(?!Apple\b)\w+', '', text)
    # Remove "#" symbols only, keeping the rest of the text
    text = text.replace("#", "")
    # Apply lemmatization
    return lemmatize_text(text)

# Apply lemmatization and cleaning to the original "Text" column
df['Text'] = df['Text'].apply(clean_and_lemmatize_text)

# Save the updated DataFrame to a new CSV file
df.to_csv('lemmatization.csv', index=False)

print("Lemmatization done, and the 'Text' column updated in the CSV file.")
