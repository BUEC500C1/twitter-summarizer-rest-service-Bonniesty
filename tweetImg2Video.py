"""
Usage: Convert image to video
@author: Tianyi Sun
"""
import os
from PIL import Image

#resize image
def process_img(name):
    dirs=os.listdir("./textImage/")
    dirs.sort()
    for paths in dirs:
        if(paths[0] == '.' or paths[0:len(name)] != name):
            continue
        img = Image.open('./textImage/'+paths)
        #resize image for ffmpeg usage
        w,h = img.size
        if w%2 ==1:
            w=w-1
        if h%2 ==1:
            h=h-1
        img = img.resize((w,h))    
        rgb_im = img.convert('RGB')
        rgb_im.save('./toVideoTweet/'+paths[0:-4]+'.jpg')
        #print("Picture: " + paths + " has been resized!")

#need to install ffmpeg before
def toVideo(account_name):
    #generate a video with 3s per frame
    #video name: tweetVideo.mp4

    command="ffmpeg -framerate 1/3 -i ./toVideoTweet/"+account_name+"pic%03d.jpg tweetVideo"+account_name+".mp4 -vf scale=900:1100"
    p=os.popen(command)
    p.close()

if __name__ == '__main__':
    name = "@AnimalPlanet"
    process_img(name)
    toVideo(name)
