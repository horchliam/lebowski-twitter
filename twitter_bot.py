import tweepy as tp
import time
import os
import random

#TODO: A feature where the bot will thank and follow anyone who follows him, will be done every day or so
#TODO: The current way of uploading pictures is not what I would like, a cleaner way would be to mine photos from online
#TODO: Fix the bot so it can be left running and so it doesn't need to be run manually
#TODO: Would like to analyze followers tweets but do not know if I'm allowed this access, ran into a 'Rate limit exceeded' error, will look into this more

disImgs = '' #Location of distorted images

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tp.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tp.API(auth)

def postPicture():
    os.chdir(disImg)
    fileCount = 0
    while fileCount < 3:
        found = False
        while not found:
            randNum = random.randint(0, len(os.listdir(disImg)) - 1)
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

# Work in progress
def thankFollowers():
    followers = api.followers()
    for follower in followers:
        folDict = follower.__dict__
        name = str(folDict['screen_name'])
        if folDict['following'] == False and folDict['follow_request_sent'] == False:
            print('Not following ' + name + '. Attempting to follow...')
            api.create_friendship(name)
            try:
                api.send_direct_message(name, 'Hey my fellow Dude, thanks for following me! Say lets go bowling sometime, the white russians will be on me!')
            except:
                print('Cannot send DM, tweepy outdated')

thankFollowers()
postPicture()
