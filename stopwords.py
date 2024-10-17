import pandas as pd
import nltk
from nltk.corpus import stopwords

# Download the stopwords if you haven't already
nltk.download('stopwords')

# Load your CSV file
csv_file = '/Users/wiktoria/Documents/master/Master thesis/January 27, 2010 - iPad announcement/January_27_2010_merged_links+apple+query+nick+dup+ASCII+lowercase.csv'  # Change to your actual file path
df = pd.read_csv(csv_file)

# Define stop words
stop_words = set(stopwords.words('english'))

# Function to remove stop words from text
def remove_stop_words(text):
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

# Apply the function to the 'Text' column
df['Text'] = df['Text'].apply(remove_stop_words)

# Save the updated DataFrame to a new CSV file
df.to_csv('stopwords_removed.csv', index=False)

print("Stop words removed and saved to a new CSV file.")
