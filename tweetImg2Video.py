"""
Usage: Convert image to video
@author: Tianyi Sun
"""
import os
from PIL import Image

#resize image
def process_img(name):
    dirs=os.listdir(os.path.dirname(__file__)+"/textImage/")
    dirs.sort()
    for paths in dirs:
        if(paths[0] == '.' or paths[0:len(name)] != name):
            continue
        img = Image.open(os.path.dirname(__file__)+'/textImage/'+paths)
        #resize image for ffmpeg usage
        w,h = img.size
        if w%2 ==1:
            w=w-1
        if h%2 ==1:
            h=h-1
        img = img.resize((w,h))
        rgb_im = img.convert('RGB')
        rgb_im.save(os.path.dirname(__file__)+'/toVideoTweet/'+paths[0:-4]+'.jpg')
    return "Image Resized!!"

#need to install ffmpeg before
def toVideo(account_name):
    #generate a video with 3s per frame
    #video name: tweetVideo.mp4
    dirs = os.listdir(os.path.dirname(__file__)+"/toVideoTweet/")
    name = account_name+"pic000.jpg"
    print(name)
    if name not in set(dirs):
        return "Fail!!!"
    command="ffmpeg -framerate 1/3 -i "+os.path.dirname(__file__)+"/toVideoTweet/"+account_name+"pic%03d.jpg " + os.path.dirname(__file__)+"/static/tweetVideo"+account_name+".mp4 -vf scale=900:1100"
    p=os.popen(command)
    p.close()
    return "Video Created!!"



if __name__ == '__main__':
    name = "@KendallJenner"
    process_img(name)
    toVideo(name)
