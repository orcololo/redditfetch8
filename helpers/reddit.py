import praw
from commonConfig import CommonConfig
from downloader import concurrent_download
from info import getInfo
import json

reddit = praw.Reddit(client_id=CommonConfig.CLIENT_ID,
                     client_secret=CommonConfig.CLIENT_SECRET,
                     user_agent=CommonConfig.AGENT_USER)


def getSub(targetSub, totalSize=None):
    count = 0
    for submissions in reddit.subreddit(targetSub).hot(limit=totalSize):
        if not submissions.stickied:
            count += 1
            print(getInfo(submissions))
    print(count)


def getUser():
    pass


def getUserAndType():
    pass


def getSub2(targetSub, totalSize=20):
    actual = 0
    linksdict = {}
    for submissions in reddit.subreddit(targetSub).hot(limit=totalSize):
        if not submissions.stickied:
            linksdict[str(targetSub)] = {
                linksdict[actual]: {'id': submissions.id, 'title': submissions.title, 'url': submissions.url,
                                    'domain': 'dunno yet'}}
            actual += 1
    return linksdict


def download(links):
    concurrent_download(links)
