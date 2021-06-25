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
        # attempts to retweet tweet mention is in reply to
        try:
            # finds the original post's id
            opId = mention.in_reply_to_status_id
            # ensures the original poster is not the bot and the post is a top-level tweet
            if opId != botId() and opId.in_reply_to_status_id is None:
                # if it's not, then it retweets the original post
                retweet(opId)
            
        # If an error happens (usually when the tweet has already been retweeted)
        # then it does nothing
        except:
            pass
    # waits 5 seconds
    # (may want to make this longer, perhapse tweets once every 10 minutes instead
    # or even once every day)
    time.sleep(5)
