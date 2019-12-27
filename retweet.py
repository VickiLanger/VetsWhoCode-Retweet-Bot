'''
retweet.py: retweet bot to retweet #VetsWhoCode
26 December 2019
Vicki Langer (@vicki_langer)
'''

import tweepy
from time import sleep
from keys import *
from os import environ

consumer_key = environ['CONSUMER_KEY']
consumer_secret = environ['CONSUMER_SECRET']
access_token = environ['ACCESS_KEY']
access_token_secret = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)


def main():
    search_term = ("#VetsWhoCode", "#vetsWhoCode")
    number_of_tweets = 5

    for tweet in tweepy.Cursor(api.search, search_term).items(number_of_tweets):
        try:
            print('\nFound tweet by @' + tweet.user.screen_name)
            tweet.retweet()
            print("Yay! Tweet was retweeted :)")

            # sleep is measured in seconds
            sleep(10)

        except tweepy.TweepError as error:
            print('wtf, why isn\'t it working?')
            print(error.reason)

        except StopIteration:
            break


main()
