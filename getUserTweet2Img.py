"""
Usage: Fetch user twitter feed and convert into image
@author: Tianyi Sun
"""

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import tweepy 
import urllib
import os
import configparser
#convert text into an image in a self designed frame
def text2img(origin_text, account_name,index):
    text= ''
    i = 0
    #make text appear in seperate lines
    while i < len(origin_text):
        text = text + origin_text[i:i+30] + '\n'
        i = i+30
    #library fonts
    #font=ImageFont.truetype("/Users/tysun/Library/Fonts/DejaVuSerif-BoldItalic.ttf", 15)
    font=ImageFont.truetype(os.path.dirname(__file__)+"/Arial.ttf", 15)
    im1 = Image.open(os.path.dirname(__file__)+"/bg1.png")
    draw = ImageDraw.Draw(im1)
    str = account_name + " by Tianyi Sun"
    draw.text((1, 1), str, (255, 165, 0), font=font)
    im1.save(os.path.dirname(__file__)+"/bg2.png")

    im1=Image.open(os.path.dirname(__file__)+"/bg2.png")
    draw=ImageDraw.Draw(im1)
    draw.text((20,80),text,(0,0,128),font=font)
    im1.save(os.path.dirname(__file__)+"/textImage/"+account_name+"pic%03d.png"%index)
    return "Image Generated!!"

#fetch tweets
def get_all_tweets(account_name, config):

    #authorization
    auth = tweepy.OAuthHandler(config.get('auth', 'consumer_key'), config.get('auth', 'consumer_secret'))
    auth.set_access_token(config.get('auth', 'access_token'), config.get('auth', 'access_secret'))
    api = tweepy.API(auth)
    #fetch 20 tweets of user
    alltweets = []
    print(account_name)
    new_tweets = api.user_timeline(screen_name = account_name,count=20)
    alltweets.extend(new_tweets)
    index = 0
    print(len(alltweets))
    #save user tweets and picture
    for status in alltweets:
        #convert text and download
        text = status.text
        if len(text) != 0:
            text2img(text,account_name,index)
            index += 1
    print("Finished Fetching Twitter Feed!!")


def getUserTwAPI(account_name, keysFileName):
    config = configparser.ConfigParser()
    config.read(os.path.dirname(__file__)+"/"+keysFileName)
    try:
        #if no credential, just return
        if len(config.get('auth','consumer_key')) == 0:
            return("")
        get_all_tweets(account_name, config)
        return("success!")
    except Exception as e:
        print(e)
        print("The account or keys is invalid!!")
        return str(e)
        #return str(Exception)
        #return("The account or keys is invalid!!")
        
                         

if __name__ == '__main__':
    #input account name and credential file name
    getUserTwAPI("@KendallJenner", "keys")

