#!/usr/bin/python3
"""
this module adds a function
"""
import json
from pprint import pprint
import requests


def number_of_subscribers(subreddit):
    """ this function queries reddit for subscribers of given subreddit """
    reddit = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    u_head = {'User-Agent': 'Stacipoo'}
    red_req = requests.get(reddit, headers=u_head, allow_redirects=False)
    if red_req.status_code is not 200:
        return (0)
    red_json = red_req.json()
    key = 'data'
    if key in red_json:
        data = red_json.get(key)
        num = data.get('subscribers')
        return (num)
