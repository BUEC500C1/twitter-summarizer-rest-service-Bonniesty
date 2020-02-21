from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import tweepy 
import urllib


#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


#convert text into an image in a self designed frame
def text2img(origin_text, index):
    text= ''
    i = 0
    #make text appear in seperate lines
    while i < len(origin_text):
        text = text + origin_text[i:i+30] + '\n'
        i = i+30     
    #library fonts
    font=ImageFont.truetype("/Users/tysun/Library/Fonts/DejaVuSerif-BoldItalic.ttf", 15)
    im1=Image.open("bg.png")
    draw=ImageDraw.Draw(im1)
    draw.text((20,80),text,(255,165,0),font=font)
    im1.save("./textImage/pic%03d.png"%index)

#fetch tweets
def get_all_tweets(account_name):

    #authorization
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #fetch 20 tweets of user
    alltweets = []
    new_tweets = api.user_timeline(screen_name = account_name,count=20)
    alltweets.extend(new_tweets)
    index = 0
    #save user tweets and picture
    for status in alltweets:
        #convert text and download
        text = status.text
        if len(text) != 0:
            text2img(text,index)
            index += 1
        #dowmload picture
        mediaData = status.entities.get('media',[])
        if(len(mediaData) != 0):  
            pic = mediaData[0]['media_url']
            urllib.request.urlretrieve(pic,"./textImage/pic%03d.png"%index)
            index += 1

    print("Finished Loading!!")  


def getUserTwAPI(account_name):
    try:
        get_all_tweets(account_name)
        return("success!")
    except Exception:
        print("The account is invalid!!")
        
                         

if __name__ == '__main__':   
    getUserTwAPI("@AnimalPlanet")

