from functions import *
import time

hashtags = ["#EAjobs"]

# constantly loops through this code
while True:
    # looks through each hashtag
    for hashtag in hashtags:
        # retweets instances of that hashtag found in past 7 days
        retweetHashtag(hashtag)
    # waits 5 seconds
    # (may want to make this longer, perhapse tweets once every 10 minutes instead
    # or even once every day)
    time.sleep(5)
