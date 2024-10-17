import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load the CSV file with tweets
csv_file = "/Users/wiktoria/Documents/master/Master thesis/August 31, 2014 - iCloud leak/August_24_2014_merged_links+apple+query+nick+dup+ASCII+lowercase+stopwords.csv"
df = pd.read_csv(csv_file)

# Initialize the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to analyze sentiment
def analyze_sentiment(tweet):
    return analyzer.polarity_scores(tweet)

# Apply the sentiment analysis to each tweet and store the results in new columns
df['Sentiment'] = df['Text'].apply(lambda tweet: analyze_sentiment(tweet))
df['Positive'] = df['Sentiment'].apply(lambda score: score['pos'])
df['Negative'] = df['Sentiment'].apply(lambda score: score['neg'])
df['Neutral'] = df['Sentiment'].apply(lambda score: score['neu'])
df['Compound'] = df['Sentiment'].apply(lambda score: score['compound'])

# Convert the 'Created_At' column to a datetime object (adjust format if necessary)
df['Created_At'] = pd.to_datetime(df['Created_At'])

# Group by date and calculate the average sentiment scores per day
daily_sentiment = df.groupby(df['Created_At'].dt.date).agg({
    'Positive': 'mean',
    'Negative': 'mean',
    'Neutral': 'mean',
    'Compound': 'mean'
}).reset_index()

# Save the tweet-level sentiment results to a new CSV file
tweet_output_file = "sentiment_per_tweet.csv"
df.to_csv(tweet_output_file, index=False)

# Save the daily sentiment results to another CSV file
daily_output_file = "sentiment_per_day.csv"
daily_sentiment.to_csv(daily_output_file, index=False)

print(f"Sentiment analysis per tweet saved to {tweet_output_file}")
print(f"Sentiment analysis per day saved to {daily_output_file}")
