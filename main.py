#! /usr/bin/env python

from twitter import *
from pprint import pprint
import sys

# Define OAuth credentials (update these with your keys)
OAUTH_TOKEN = ''
OAUTH_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

# Initialize Twitter API
t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

# Constants
TWEET_COUNT = 200

def fetch_user_tweets(screen_name):
    """Fetches tweets from a user's timeline."""
    try:
        return t.statuses.user_timeline(count=TWEET_COUNT, screen_name=screen_name)
    except Exception as e:
        print(f"Error fetching tweets: {e}")
        return []

def calculate_engagement(tweets, username):
    """Calculates the average favorites and retweets for a user's tweets."""
    count = 0
    total_favorites = 0
    total_retweets = 0

    for tweet in tweets:
        # Only count tweets by the specified user, excluding retweets
        if tweet['user']['screen_name'] == username and not tweet['text'].startswith("RT"):
            count += 1
            total_favorites += tweet['favorite_count']
            total_retweets += tweet['retweet_count']

    # Avoid division by zero
    avg_favorites = total_favorites / count if count > 0 else 0
    avg_retweets = total_retweets / count if count > 0 else 0

    return avg_favorites, avg_retweets

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <Twitter_Username>")
    else:
        username = sys.argv[1]
        tweets = fetch_user_tweets(username)
        avg_favs, avg_rts = calculate_engagement(tweets, username)

        print(f"Average Favorites: {avg_favs:.2f}")
        print(f"Average Retweets: {avg_rts:.2f}")
