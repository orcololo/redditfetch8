import praw
from helpers.commonConfig import CommonConfig
from helpers.downloader import concurrent_download
from helpers.info import getInfo
import json

reddit = praw.Reddit(client_id=CommonConfig.CLIENT_ID,
                     client_secret=CommonConfig.CLIENT_SECRET,
                     user_agent=CommonConfig.AGENT_USER)


def getSub(targetSub, totalSize=None):
    count = 0
    result = {}
    links = []
    for submission in reddit.subreddit(targetSub).hot(limit=totalSize + 2):
        if not submission.stickied:
            count += 1
            links.append(submission.url)
            result[f'{count}'] = getInfo(submission)
    return result, links


def getUser():
    pass


def download(links):
    concurrent_download(links)
