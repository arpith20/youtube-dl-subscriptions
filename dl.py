from __future__ import unicode_literals
import opml
import feedparser
import youtube_dl
from glob import glob
from pprint import pprint

from time import time, mktime, strptime
from datetime import datetime

if len(glob('last.txt')) == 0:
    f = open('last.txt', 'w')
    f.write(str(time()))
    print('Initialized a last.txt file with current timestamp.')
    f.close()

else:
    f = open('last.txt', 'r')
    content = f.read()
    f.close()

    outline = opml.parse('subscription_manager')

    ptime = datetime.utcfromtimestamp(float(content))
    ftime = time()

    urls = []

    for i in range(0,len(outline[0])):
        urls.append(outline[0][i].xmlUrl)

    count = 0
    for i in range(0,len(urls)):
        print('Parsing through channel '+str(i+1)+' out of '+str(len(urls)), end='\r')
        feed = feedparser.parse(urls[i])
        for j in range(0,len(feed['items'])):
            timef = feed['items'][j]['published_parsed']
            dt = datetime.fromtimestamp(mktime(timef))
            if dt > ptime:
                ydl_opts = {
                    'outtmpl': str(dt) + '--%(uploader)s--%(title)s.%(ext)s'
                }
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([feed['items'][j]['link']])
                count = count + 1 

    if count == 0:
        print('\nSorry, no new video found')
    else:
        print('\n' + str(count)+' new video(s) found')

    f = open('last.txt', 'w')
    f.write(str(ftime))
    f.close()
