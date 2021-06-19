import tweepy
from config import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

def tweet(text):
    # authentification
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # getting tweepy api object
    api = tweepy.API(auth)

    # posting tweet
    api.update_status(text)

# returns all tweets made after or on the date entered, sorted from newest (0) to oldest (99), when return when text is searched using Twitter's search capability
# data types: returns 2d array with tweet id in the first row (as an integer), and the tweet text in the second row (as a string)
# date input is in yyyy-mm-dd format, and a string if it is used
def search(text, date=Null):
    # authentification
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # getting tweepy api object
    api = tweepy.API(auth)

    # limiting to 100 items, since more seems overkill
    max_results = 100
    results = list()

    # Using twitter search function to search for inputted text
    for i,tweet in enumerate(tweepy.Cursor(api.search, q=text, since=date).items(max_results)):
        results.append([tweet.id, tweet.text])

    return results

# retweets a tweet, given it's id
def retweet(id):
    # authentification
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # getting tweepy api object
    api = tweepy.API(auth)

    api.retweet(id)

# saves a tweet id to a file
# this will be important so we don't accidentally re-retweet a tweet
def remember(fileName, id):
    f = open(fileName, 'a')
    f.write(str(id) + "\n")
    f.close()
