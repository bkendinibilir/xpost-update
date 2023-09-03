#!/usr/bin/python

import os
import sys
import json
import tweepy

secrets = {
    'consumer_key': os.environ.get("CONSUMER_KEY"),
    'consumer_secret': os.environ.get("CONSUMER_SECRET"),
    'access_token': os.environ.get("ACCESS_TOKEN"),
    'access_token_secret': os.environ.get("ACCESS_TOKEN_SECRET"),
}
secrets_filename=os.environ.get('SECRETS_FILE')
post_id=os.environ.get('POST_ID')
post_text=os.environ.get('POST_TEXT')

if(len(sys.argv) > 1):
    post_text=sys.argv[1]

if(not post_text):
    print("ERROR: No post text given in env POST_TEXT or first command line argument.")
    exit(1) 

if secrets_filename:
    try:
        with open(secrets_filename, 'r') as f:
            secrets = json.load(f)
            f.close()
    except:
        print("FATAL: cannot open secrets file '{}'.".format(secrets_filename))
        exit(1)

for key, value in secrets.items():
    if(not value or len(value) == 0):
        print("FATAL: No {} given as env or in a SECRETS_FILE.".format(key.upper()))
        exit(1)

client = tweepy.Client(
    consumer_key=secrets['consumer_key'], 
    consumer_secret=secrets['consumer_secret'],
    access_token=secrets['access_token'], 
    access_token_secret=secrets['access_token_secret']
)

try:
    with open('data/lastpost_id', 'r') as f:
        lastpost_id = f.read()
        client.delete_tweet(lastpost_id)
        f.close()
except:
    if(post_id):
        client.delete_tweet(post_id)

response = client.create_tweet(user_auth=True, text=post_text)

with open('data/lastpost_id', 'w') as f:
    f.write(str(response.data['id']))
    f.close()
