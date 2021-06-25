from functions import *
import time

# Enter hashtags to be retweeted in this list.
hashtags = ["#EAjobs"]

# constantly loops through this code
while True:
    # looks through each hashtag
    for hashtag in hashtags:
        # retweets instances of that hashtag found in past 7 days
        retweetHashtag(hashtag)

    # loops through all the mentions of the bot on the timeline
    for mention in mentions():
        # attempts to retweet mention
        try:
            # but only if it isn't in reply to anything
            if mention.in_reply_to_status_id is None:
                retweet(mention.id)
        # If an error happens (usually when the tweet has already been retweeted)
        # then it does nothing
        except:
            pass
    # waits 5 seconds
    # (may want to make this longer, perhapse tweets once every 10 minutes instead
    # or even once every day)
    time.sleep(5)
