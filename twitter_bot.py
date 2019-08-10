import tweepy as tp
import time
import os
import random
from selenium import webdriver
import smtplib
import pyautogui

#TODO: Email me whats trending. Email my sister tweets that I think she might enjoy

#TODO: A feature where the bot will thank and follow anyone who follows him, will be done every day or so
#TODO: The current way of uploading pictures is not what I would like, a cleaner way could be to mine photos from online
#TODO: Fix the bot so it can be left running and so it doesn't need to be run manually (rasberry pi?)

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

# This method will comment on the most recent tweet that pertains to the topic of python
def commentRandomTweets():
    browser = webdriver.Firefox(executable_path=r'/Users/liamhorch/Downloads/geckodriver')
    browser.get('https://twitter.com/login')
    userField = browser.find_element_by_css_selector('.js-username-field')
    userField.send_keys('My username')
    passField = browser.find_element_by_css_selector('.js-password-field')
    # These excessive sleep calls were necessary for without them the script ran too fast for the browser
    time.sleep(2)
    passField.send_keys('My password')
    time.sleep(2)
    passField.submit()
    time.sleep(2)
    browser.get('https://twitter.com/search?q=python&f=live')
    time.sleep(2)
    # I could not find the css selector for the comment button so I instead chose to take a shot in the dark and
    # click a preset location which always should be the location of the first tweet
    pyautogui.moveTo(850, 220, duration = 3)
    time.sleep(2)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(2)
    try:
        comment = browser.find_element_by_css_selector('div.r-3qxfft:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > svg:nth-child(2)')
        comment.click()
        comText = browser.find_element_by_css_selector('.notranslate')
        comText.send_keys('Hey we should go bowling sometime.')
        time.sleep(1)
        pyautogui.hotkey('command', 'enter')
        time.sleep(1)
    except:
        print('Uncommentable tweet')
    browser.close()
        
# Work in progress, my sister does not use twitter but I'm sure she would love these images, so I plan to email them to her
def sendKeelyImages():
    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.ehlo()
    conn.starttls()
    conn.login('my email', 'her email')
    conn.sendmail('my email', 'her email', 'subject')
    conn.quit()

thankFollowers()
postPicture()
commentRandomTweets()
