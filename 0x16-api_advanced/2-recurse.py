#!/usr/bin/python3
"""
this module adds a function
"""
import json
import requests


def recurse_you(subreddit, hot_list=[]):
    """ this function queries reddit for 10 hot posts of given subreddit """
    reddit = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    u_head = {'User-Agent': 'Stacipoo'}
    red_req = requests.get(reddit, headers=u_head, allow_redirects=False)
    if red_req.status_code is not 200:
        print('None')
        return
    red_json = red_req.json()
    key = 'data'
    if key in red_json:
        data = red_json.get(key)
        chil = data.get('children')
    for info in chil:
        hot_title = info.get("data").get("title")
        print(hot_title)
