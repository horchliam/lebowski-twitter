#!/Users/liamhorch/tweepy-bots/venv/lib/python3.7

import tweepy as tp
import time
import os
import random

disImg = '/Users/liamhorch/Desktop/my_bot_polished/lebowski_distorted_pics'

CONSUMER_KEY = 'bK2md1ZY0ZIks19IiH5BhUev6'
CONSUMER_SECRET = 'I5fa4LV80AWosnbD0gGHHzXUks0p9EeXSI5l7wJOapzweFTDCB'
ACCESS_KEY = '1152433490748694529-v3JcKdfipyKIQhR3Aw7WO8QusOPYLe'
ACCESS_SECRET = 'fCoDYcwfAnbdkVJMXo7N4DqUaylrNBrOZ8OFx1X6VP0c8'

auth = tp.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tp.API(auth)

os.chdir(disImg)
fileCount = 0
#for file in range(0, len(os.listdir(disImg)) - 1):
while fileCount < 3:
#    if str(file) == '.DS_Store':
#        continue
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

#leQuotes = open("lebowski_quotes.txt", "r").readlines()
#for line in leQuotes:
    #api.update_status(line)
#    print(line)
#    time.sleep(random.randrange(3600, 7200, 600))

#leQuotes.close()
