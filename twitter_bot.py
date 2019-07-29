import tweepy as tp
import time
import os
import random

disImgs = '' #Location of distorted images

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tp.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tp.API(auth)

os.chdir(disImg)
fileCount = 0
while fileCount < 3:
    found = False
    while not found:
        randNum = random.randint(1, len(os.listdir(disImg)) - 1)
        pic = '/Users/liamhorch/Desktop/my_bot_polished/lebowski_distorted_pics/distort%d.jpg' % randNum
        if not os.path.exists(pic):
            continue
        else:
            found = True
            api.update_with_media(pic)
            os.rename('distort%d.jpg' % randNum, 'USED%d.jpg' % randNum)
            print('posting picture ...')
            fileCount += 1
            time.sleep(random.randrange(180, 360))
