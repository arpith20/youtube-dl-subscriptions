# youtube-dl-subscriptions
Downloads all new videos from your YouTube subscription feeds.

I recommend to create a new folder and place the dl.py inside. You will also need a OPML file named `subscription_manager` containing all your YouTube's subscriptions in the same folder. You can download it from https://www.youtube.com/subscription_manager?action_takeout=1 when you're logged in your YouTube account. The script will create a last.txt file inside the folder in order to remember when it was last run and not re-download the same videos again.

Dependencies:
* opml
* feedparser
* youtube-dl
