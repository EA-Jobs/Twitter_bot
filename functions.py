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

# returns 2d array with tweet id in the first row (as an integer), and the tweet text in the second row (as a string)
def search(text):
    # authentification
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # getting tweepy api object
    api = tweepy.API(auth)

    # limiting to 100 items, since more seems overkill
    max_results = 100
    results = list()

    # Using twitter search function to search for inputted text
    for i,tweet in enumerate(tweepy.Cursor(api.search, q=text).items(max_results)):
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
