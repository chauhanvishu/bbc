# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 22:42:25 2018

@author: aksha
"""

import tweepy
from datetime import datetime, date, time, timedelta
import sys
import textblob
#The actual keys & secrets aren't shared for obvious reasons here
consumer_key = "tR0N4gxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
consumer_secret = "8qvl96Rkvxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_key = " 861540811514xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_secret = " 1BteblELkbxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)
api=tweepy.API(auth)
account_list = []
if (len(sys.argv) > 1):
    account_list = sys.argv[1:]
else:
    print("Please provide a list of usernames at the command line.")
    sys.exit(0)
if len(account_list) > 0:
    for target in account_list:
        print("Getting data for " + target)
        item = auth_api.get_user(target)
        print("name: " + item.name)
        print("screen_name: " + item.screen_name)
        print("description: " + item.description)
        print("statuses_count: " + str(item.statuses_count))
        print("friends_count: " + str(item.friends_count))
        print("followers_count: " + str(item.followers_count))
