#!/usr/bin/python3
"""
this module adds a function
"""
import json
import requests


def recurse(subreddit, hot_list=[]):
    """ this function queries reddit for 10 hot posts of given subreddit """
    reddit = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    u_head = {'User-Agent': 'Stacipoo'}
    red_req = requests.get(reddit, headers=u_head, allow_redirects=False)
    if red_req.status_code is not 200:
        return ('None')
    red_json = red_req.json()
    if 'after' in red_json["meta"]["pagination"]:
        after = red_json["meta"]["pagination"]["after"]
        hot_list.append(after)
    return (recurse(subreddit, hot_list=[]))
