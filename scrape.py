import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# List of target dates
dates = [
    ("August 24, 2011", "2011-08-17", "2011-08-31"),
    ("January 27, 2010", "2010-01-20", "2010-02-03"),
    ("August 31, 2014", "2014-08-24", "2014-09-07"),
    ("March 5, 2010", "2010-02-26", "2010-03-12"),
    ("August 3, 2011", "2011-07-27", "2011-08-10"),
    ("May 12, 2014", "2014-05-05", "2014-05-19"),
]

# Queries
queries = ["Apple", "iPhone", "iPad", "iCloud"]

# Function to scrape tweets based on a Twitter search URL
def scrape_tweets(url, csv_filename, tweet_limit=5000):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    tweets = []
    count = 0

    # Parse the tweet data
    for tweet in soup.find_all('div', class_='tweet'):
        if count >= tweet_limit:
            break
        tweet_text = tweet.find('p', class_='tweet-text').text
        tweet_time = tweet.find('span', class_='tweet-timestamp').text

        tweets.append({
            'Text': tweet_text,
            'Timestamp': tweet_time
        })
        count += 1

    # Save the data to a CSV file
    df = pd.DataFrame(tweets)
    df.to_csv(csv_filename, mode='a', index=False, header=False)

# Loop over dates and queries
for date_name, start_date, end_date in dates:
    for query in queries:
        twitter_url = f"https://twitter.com/search?q={query}%20since%3A{start_date}%20until%3A{end_date}%20lang%3Aen&src=typed_query&f=live"
        csv_filename = f"tweets_{date_name.replace(' ', '_')}_{query}.csv"
        scrape_tweets(twitter_url, csv_filename)
        time.sleep(10)  # Pause to avoid rate limits
