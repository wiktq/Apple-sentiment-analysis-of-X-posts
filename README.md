# Apple - sentiment analysis of X posts using VADER

##Content
1) Scrapping tweets for multiple archival dates (steps with asterisks are optional if the code fails).
2) Data cleaning (including non ASCII characters removal, lemmatization, and more).
3) Sentiment analysis using VADER
4) Random sample retrival for calcculating F! score (or any other model's accuracy measure).

### IMPORTANT - Always ensure that you use the correct file directory in the scripts.

## Data fetching
1. Cloning the repository from GitHub
```bash
git clone https://github.com/wiktq/Apple-sentiment-analysis.git
   cd Apple-sentiment-analysis
```
2. Creation and activation of virtual environment for macos
```bash
python -m venv venv
    source venv/bin/activate
```
3. Installing packages
```bash
pip install -r requirements.txt
```
4. Running the script on the terminal 
```bash
python scrape.py
```
*5. Blocking - 
I would suggest to lower the data volume in the code to minimize the probability of twitter's ban. If decreasing the volume is not possible, add a new twitter account data to the "credentials.py" after every block.

*6. Deleting the repository from Mac, if needed
```bash
rm -rf Apple-sentiment-analysis
```
*7. Fetching the latest changes from GitHub
```bash
git pull origin main
```
8. Merging the output csv files, if they were downloaded separately
```bash
python csvmerge.py
```

## Data cleaning 
1. Since "Apple" is a polysemous term (having multiple meanings), it is important to apply smart query filtering. The query.py script filters out exported tweets that contain specific queries listed in the script, which are deemed irrelevant to the topic. These queries are excluded based on both personal knowledge and internet research. Additionally, an extra script, wordfrequency.py, should be used to analyze the most common words in the posts and identify any terms (like "caramel") that could suggest the posts are unrelated to the company's topic.
```bash
python wordfrequency.py
python query.py
```
2. Next step is to delete all links (queries starting with "http") and mentions (besides @Apple) to prevent distortion. 
```bash
python links.py
python nick.py
```
3. Delete the duplicated posts
```bash
python duplicate.py
```
4. Remove all non-ASCII characters to improve the effectiveness of VADER sentiment analysis.
```bash
python nonASCII.py
```
5. Case folding - normalizing the text and putting all posts into lowercase
```bash
python lowercase.py
```
6. Removing the stop words (like "at", "the", "and" etc.)
```bash
python stopwords.py
```
7. Lemmatization - preprocessing technique, reducing a word to its base or root form, known as the "lemma."
```bash
python lemmatization.py
```
8. You can do one final filtering based on the presence of the query "Apple" (just to be sure).
```bash
python apple.py
```

## Sentiment

You can check the sentiment of fetched posts using the VADER model. In the script used in this repository, the outcome of the sentiment will be in a form of a compound (numeric value ranging from -1 to 1). The sentiment is provided for every tweet. 
```bash
python sentiment.py
```

## Accuracy of the model 

To assess the model's accuracy, use the additional script provided. Since the total number of tweets could reach tens of thousands, manually labeling each one is not feasible. Instead, use the randomtweets.py script to select a random sample for calculating the F1 score. 
However, if possible, calculate the F1 score for the entire dataset rather than just the sample.
```bash
python randomtweets.py
```

