import cv2
import os

movie = '' #Location of The Big Lebowski film

def frameCapture(path):
    video = cv2.VideoCapture(path)
    count = 0
    fileNum = 0
    success = True

    while success:
        success, image = video.read()
        if(count % 200 == 0):
            name = 'frame%d.jpg' % fileNum
            print('uploading ...' + name)
            cv2.imwrite(name, image)
            fileNum += 1
        count += 1

def clearFolder(path):
    for file in os.listdir(path):
        os.remove(file)

if not os.path.exists('unused_imgs'):
    os.makedirs('unused_imgs')

os.chdir('/Users/liamhorch/Desktop/my_bot_polished/unused_imgs')
clearFolder('/Users/liamhorch/Desktop/my_bot_polished/unused_imgs')
frameCapture(movie)
print('Finished!')
