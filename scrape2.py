import asyncio
import csv
import logging
import random
import json
from twikit import Client, TooManyRequests
from datetime import datetime
from typing import List, Tuple, Optional
from credentials import (
    RAW_DIR,
    COOKIES_FILE,
    RESUME_FILE,
    TWITTER_USERNAME,
    TWITTER_EMAIL,
    TWITTER_PASSWORD,
)

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Set minimum value of tweets you want to get per query
MINIMUM_TWEETS = 500  # Adjust based on your goal of 20k-30k total tweets

# List of queries and filenames for each search
QUERIES: List[Tuple[str, str]] = [
    ("min_faves:10 'Apple' lang:en until:2011-08-30 since:2011-08-28", "aug_24_2011.csv"),
    ("min_faves:10 'Apple' lang:en until:2010-02-02 since:2010-01-31", "jan_27_2010.csv"),
    ("min_faves:10 'Apple' lang:en until:2014-09-03 since:2014-09-01", "aug_31_2014.csv"),
    ("min_faves:10 'Apple' lang:en until:2010-03-09 since:2010-03-07", "mar_5_2010.csv"),
    ("min_faves:10 'Apple' lang:en until:2011-08-09 since:2011-08-07", "aug_3_2011.csv"),
    ("min_faves:10 'Apple' lang:en until:2014-05-17 since:2014-05-15", "may_12_2014.csv"),
]

async def get_tweets(client: Client, query: str, tweets: Optional[object]) -> object:
    if tweets is None:
        logging.info(f"Getting tweets for query: {query}")
        tweets = await client.search_tweet(query, product="Latest")
    else:
        wait_time = random.randint(5, 25)
        logging.info(
            f"Getting next tweets for query: {query} after {wait_time} seconds"
        )
        await asyncio.sleep(wait_time)
        tweets = await tweets.next()
    return tweets

async def scrape_tweets(query: str, filename: str) -> None:
    client = Client(language="en-US")
    await client.login(
        auth_info_1=TWITTER_USERNAME,
        auth_info_2=TWITTER_EMAIL,
        password=TWITTER_PASSWORD,
    )
    client.save_cookies(str(COOKIES_FILE))

    tweet_count = 0
    tweets = None

    full_path = RAW_DIR / filename

    if RESUME_FILE.exists():
        with RESUME_FILE.open("r") as f:
            resume_state = json.load(f)
        if resume_state["query"] == query:
            tweet_count = resume_state["tweet_count"]
            logging.info(f"Resuming scraping for {query} from tweet {tweet_count}")

    with full_path.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if tweet_count == 0:
            writer.writerow(
                ["Tweet_Count", "Username", "Text", "Created_At", "Retweets", "Likes"]
            )

        while tweet_count < MINIMUM_TWEETS:
            try:
                tweets = await get_tweets(client, query, tweets)
            except TooManyRequests as e:
                rate_limit_reset = datetime.fromtimestamp(e.rate_limit_reset)
                logging.warning(f"Rate limit reached. Waiting until {rate_limit_reset}")
                wait_time = (rate_limit_reset - datetime.now()).total_seconds()
                await asyncio.sleep(wait_time)
                continue
            except Exception as e:
                logging.error(f"Error fetching tweets: {str(e)}")
                await asyncio.sleep(60)
                continue

            if not tweets:
                logging.info(f"No more tweets found for query: {query}")
                break

            for tweet in tweets:
                tweet_count += 1
                tweet_data = [
                    tweet_count,
                    tweet.user.name,
                    tweet.text,
                    tweet.created_at,
                    tweet.retweet_count,
                    tweet.favorite_count,
                ]
                writer.writerow(tweet_data)

            logging.info(f"Got {tweet_count} tweets for query: {query}")

            with RESUME_FILE.open("w") as f:
                json.dump({"query": query, "tweet_count": tweet_count}, f)

    logging.info(f"Done for query: {query}. {tweet_count} tweets found")
    RESUME_FILE.unlink(missing_ok=True)

    await asyncio.sleep(15)

async def main():
    for query, filename in QUERIES:
        await scrape_tweets(query, filename)

if __name__ == "__main__":
    asyncio.run(main())
