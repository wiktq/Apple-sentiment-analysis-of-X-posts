# Apple-sentiment-analysis
Scrapping tweets and making sentiment analysis to see if Apple's market price has any dependencies over the tweets' sentiment.

Content
1) Scrapping tweets for multiple archival dates (steps with asterisks are optional if the code fails).


First steps
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
I would suggest to lower the data volumes in the code to minimize the probability of twitter's ban. If decreasing the volume is not possible, add a new twitter account data to the "credentials.py" after every block.

*6. Deleting the repository from Mac, if needed
```bash
rm -rf Apple-sentiment-analysis
```
*7. Fetching the latest changes from GitHub
```bash
git pull origin main
