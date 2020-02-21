import os
from PIL import Image

def process_img():
    dirs=os.listdir("./textImage/")
    dirs.sort()
    for paths in dirs:
        if(paths[0] == '.'):
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
        rgb_im.save('./toVideoImage/'+paths[0:6]+'.jpg')
        print("Picture: " + paths + " has been resezed!")

#need to install ffmpeg before
def toVideo():
    #generate a video with 3s per frame
    #video name: tweetVideo.mp4
    command="ffmpeg -framerate 1/3 -i ./toVideoImage/pic%03d.jpg tweetVideo.mp4 -vf scale=900:1100"
    p=os.popen(command)
    p.close()

if __name__ == '__main__':
    process_img()
    toVideo()
    
    
