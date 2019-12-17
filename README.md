# Monitoreddit


## Purpose
This little Python script for a reddit bot can monitor subreddits and check them for specific keywords.
Once a chosen keyword is dropped within the title of a new submission, the bot sends your actual user a PM with the URL to the post.

## Setup
1. Create a reddit account for your bot
2. Login in reddit with the bot
3. Visit [this](https://old.reddit.com/prefs/apps/) with your bot
4. At the bottom of the page, click ```create another app...```
5. Select ```Script```, and an appropriate name
6. Click on ```create app```

7. Download or clone this repository
8. Navigate to the root of this repository
9. Execute ```pip install -r requirements.txt```
10. Open ```__main__.py```
11. Replace ```your-user-agent-here``` with an appropriate value like [so](https://praw.readthedocs.io/en/latest/getting_started/quick_start.html)
12. Replace ```your-client-id-here``` with the value under [personal use script](https://old.reddit.com/prefs/apps/) that you just created
13. Replace ```your-secret-here``` with the value besides [secret](https://old.reddit.com/prefs/apps/) (you have to click edit on the app to see it) 
14. Replace ```bot_username``` and ```bot_password``` with the respective values of your bot account
15. Replace ```your-subreddit-here``` with the name of the subreddit you want to monitor (without r/)
16. Replace ```your, keywords, here``` with the actual keyword(s) you want to monitor the subreddit for
17. Save
18. Run ```python .``` in the folder of ```__main__.py```
