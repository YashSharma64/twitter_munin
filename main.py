#! /usr/bin/env python

from twitter import *
from pprint import pprint
import sys

from collections import OrderedDict

OAUTH_TOKEN = ''
OAUTH_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
                       CONSUMER_KEY, CONSUMER_SECRET))

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Wrong number of arguments")
    else:
        name=sys.argv[1]
        tweets = t.statuses.user_timeline(count=200,screen_name=name)
        count = 0
        favs = 0
        retweets = 0

        for t in tweets:
            #Only count tweets by me, not retweets
            if t['user']['screen_name'] == name and t['text'].find("RT") != 0:
                count += 1
                favs += t['favorite_count']
                retweets += t['retweet_count']

        print("favorite.value {}".format(favs/count))
        print("retweet.value {}".format(retweets/count))


