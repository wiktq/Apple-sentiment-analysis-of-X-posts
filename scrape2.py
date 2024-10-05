from datetime import timedelta, datetime

# Set minimum value of tweets per day
TWEETS_PER_DAY = 400

# List of key dates with their ranges (7 days before and after)
DATE_RANGES = [
    ("2011-08-17", "2011-08-31", "aug_24_2011.csv"),
    ("2010-01-20", "2010-02-03", "jan_27_2010.csv"),
    ("2014-08-24", "2014-09-07", "aug_31_2014.csv"),
    ("2010-02-26", "2010-03-12", "mar_5_2010.csv"),
    ("2011-07-27", "2011-08-10", "aug_3_2011.csv"),
    ("2014-05-05", "2014-05-19", "may_12_2014.csv"),
]

# Queries to search for
QUERIES = ["Apple", "iPhone", "iPad", "iCloud"]

async def scrape_tweets(query: str, filename: str, start_date: str, end_date: str) -> None:
    client = Client(language="en-US")
    await client.login(
        auth_info_1=TWITTER_USERNAME,
        auth_info_2=TWITTER_EMAIL,
        password=TWITTER_PASSWORD,
    )
    client.save_cookies(str(COOKIES_FILE))

    # Convert dates to datetime objects
    current_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')

    full_path = RAW_DIR / filename

    with full_path.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Tweet_Count", "Query", "Text", "Created_At"])

        while current_date <= end_date_dt:
            daily_tweet_count = 0
            daily_start = current_date.strftime('%Y-%m-%d')
            daily_end = (current_date + timedelta(days=1)).strftime('%Y-%m-%d')

            while daily_tweet_count < TWEETS_PER_DAY:
                try:
                    query_with_date = f"{query} lang:en since:{daily_start} until:{daily_end}"
                    tweets = await get_tweets(client, query_with_date, None)
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
                    logging.info(f"No more tweets found for query: {query} on {daily_start}")
                    break

                for tweet in tweets:
                    tweet_text = tweet.text.lower()
                    exclude_words = ["fruit", "juice", "tree", "pie", "cider", "orchard"]

                    if "apple" in tweet_text and not any(exclude in tweet_text for exclude in exclude_words):
                        daily_tweet_count += 1
                        tweet_data = [
                            daily_tweet_count,
                            query,
                            tweet.text,
                            tweet.created_at,
                        ]
                        writer.writerow(tweet_data)

                    if daily_tweet_count >= TWEETS_PER_DAY:
                        break

            logging.info(f"Got {daily_tweet_count} tweets for query: {query} on {daily_start}")

            # Move to the next day
            current_date += timedelta(days=1)

        logging.info(f"Done for query: {query}. Total tweets collected.")

    await asyncio.sleep(15)


async def main():
    for start_date, end_date, filename in DATE_RANGES:
        for query in QUERIES:
            await scrape_tweets(query, filename, start_date, end_date)


if __name__ == "__main__":
    asyncio.run(main())
