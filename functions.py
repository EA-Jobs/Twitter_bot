import tweepy
import datetime
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
def search(text, date=None):
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
        results.append([tweet.ident, tweet.text])

    return results

# retweets a tweet, given it's id
def retweet(ident):
    # authentification
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # getting tweepy api object
    api = tweepy.API(auth)

    api.retweet(ident)

# saves a tweet id to a file
# this will be important so we don't accidentally re-retweet a tweet
def remember(fileName, ident):
    f = open(fileName, 'w')
    f.write(str(ident) + "\n")
    f.close()

# checks to see if tweet has been retweeted already
# id input is an integer
def retweeted(fileName, ident):
    f = open(fileName, 'r')
    for remembered_id in f:
        if int(remembered_id) == ident:
            f.close()
            return True
    f.close()
    return False    

# retweets all results from a search (hashtag) which have not already been retweeted
def retweetHashtag(hashtag):
    # finds the day two days ago
    dt = datetime.datetime.now()
    d = datetime.timedelta(days=2)
    dateTwoDaysAgo = dt - d

    # converts that day into a tweepy-acceptable date format
    year = dateTwoDaysAgo.year
    month = dateTwoDaysAgo.month
    day = dateTwoDaysAgo.day
    since = str(year) + "-" + str(month) + "-" + str(day-2)

    # searches twitter for tweets with that hashtag made two days ago
    tweets = search(hashtag, date=since)

    # loops through those tweets
    for tweet in tweets:
        ident = tweet[0]
        # if the tweet has not been retweeted, 
        if not retweeted("retweeted.txt", ident):
            # then retweet the tweet
            retweet(ident)
            # and remember it's been retweeted
            remember("retweeted.txt", ident)
        else:
            # otherwise do nothing
            pass
