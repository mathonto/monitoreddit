# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Monitoring specific subreddits for certain keywords in new    #
#                                                               #
# Author: Tobias Mathony                                        #
#                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import praw
import time

user_agent = 'your-user-agent-here'
client_id = 'your-client-id-here'
client_secret = 'your-client-secret-here'
my_user_name = 'your-username-here'
bot_user_name = 'your-bot-username-here'
bot_password = 'your-bot-password-here'
subreddit = 'your-subreddit-here'
keywords = ['your', 'keywords', 'here']
already_checked = []

def checkSubreddit():
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent=user_agent,
                         username=bot_user_name,
                         password=bot_password
                         )

    for submission in reddit.subreddit(subreddit).new(limit=15):
        for keyword in keywords:
            if keyword.lower() in submission.title.lower() in submission.title.lower() and submission.created_utc not in already_checked:
                print(submission.title)
                already_checked.append(submission.created_utc)
                msg = 'Check this out {0}'.format(submission.url)
                reddit.redditor(my_user_name).message('Message', msg)
    time.sleep(60)

while True:
    checkSubreddit()
