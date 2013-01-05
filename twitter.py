#!/usr/bin/env python

from time import sleep
from sys import exit
from datetime import datetime
import tweepy

# Setting API
CONSUMER_KEY = '-'
CONSUMER_SECRET = '-'
ACCESS_KEY = '-'
ACCESS_SECRET = '-'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Serve Stack
old_stack = []

try:
	while True:
		# GET 20 Mentions
		ment = api.mentions()
		new_stack = []

		if(len(old_stack) > 0) :
			for stat in ment:
				new_stack.append(stat.id)
				if(stat.id in old_stack):
					break
				else:
					if(stat.user.screen_name!='id_twitter'):
						api.retweet(stat.id)
						print 'retweet : '+stat.text+' from '+stat.user.screen_name
					sleep(5)
			old_stack = new_stack
		else : 
			for stat in ment:
				new_stack.append(stat.id)
				if(stat.user.screen_name!='id_twitter'):
					api.retweet(stat.id)
				sleep(5)
			old_stack = new_stack
		sleep(5*60) # will update every 5 minute

except KeyboardInterrupt:
	exit()

	
