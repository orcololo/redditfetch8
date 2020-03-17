import praw
from helpers.commonConfig import CommonConfig

reddit = praw.Reddit(client_id=CommonConfig.CLIENT_ID,
                     client_secret=CommonConfig.CLIENT_SECRET,
                     user_agent=CommonConfig.AGENT_USER)


def getSub():
    pass


def getUser():
    pass


def getUserAndType():
    pass
