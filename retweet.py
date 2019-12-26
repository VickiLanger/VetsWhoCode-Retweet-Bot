'''
retweet.py: updated to be #VetsWhoCode bot
26 December 2019
Vicki Langer (@vicki_langer)
'''

import tweepy
from time import sleep

from keys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


user = api.me()
print(user.name)

def main():
    search_term = ("#VetsWhoCode", "#vetsWhoCode", "#VeteransWhoCode", "#veteransWhoCode")
    number_of_tweets = 5

    for tweet in tweepy.Cursor(api.search, search_term).items(number_of_tweets):
        try:
            print('\nRetweet Bot found tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to retweet.')
            tweet.retweet()
            print("Yay! Tweet was retweeted :)")
            
            #sleep is measured in seconds
            sleep(10)

        except tweepy.TweepError as error:
            print(error.reason)

        except StopIteration:
            break

main()

