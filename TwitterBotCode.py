#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 17:39:49 2021

@author: kyliewise
"""

import tweepy
import logging
import time
import os
import config
import requests
import json

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) # fill in tokens
auth.set_access_token(access_token, acess_token_secret) # fill in tokens

# Create API object
api = tweepy.API(auth)

logger = logging.getLogger()

def create_api():
    consumer_key = # fill in token
    consumer_secret = # fill in token
    access_token = # fill in token
    access_token_secret = # fill in token


    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api


# Create a tweet

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords[0:2]):
            try:
                logger.info(f"Answering to {tweet.user.screen_name}")

                api.update_status(
                    status="Ask us for a quote of the day, @"+ tweet.user.screen_name,
                    in_reply_to_status_id=tweet.id,
                )
            except:
                logger.info(f"Already replied to {tweet.user.screen_name}")
        elif any(keyword in tweet.text.lower() for keyword in keywords[2:4]):
            try:
                logger.info(f"Answering to {tweet.user.screen_name}")

                tweet_quote = get_quote()

                api.update_status(
                    status='@' + tweet.user.screen_name + " Here's some inspiration: " + tweet_quote,
                    in_reply_to_status_id=tweet.id,
                )
            except:
                logger.info(f"Already replied to {tweet.user.screen_name}")
    return new_since_id

def get_quote():
    URL = "https://api.quotable.io/random"
    try:
        response = requests.get(URL)
    except:
        print("Error while calling API...")

    res = json.loads(response.text)
    return res['content'] + "-" + res['author']

def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, ["help", "info", "quote","inspiration"], since_id)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()