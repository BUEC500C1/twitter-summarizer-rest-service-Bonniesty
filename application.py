'''
reference:
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html#python-flask-deploy
https://flask.palletsprojects.com/en/1.1.x/quickstart/
'''
from flask import Flask
import getUserTweet2Img as twitter_api
import tweetImg2Video as video_api
from markupsafe import escape
from flask import render_template
from flask import request

# EB looks for an 'application' callable by default.
application = Flask(__name__, static_folder='static')

#call twitter api
def call_twt_api(username):
    str1 = "Fail!!!"
    if username != "" and username[0] == "@":
        status = twitter_api.getUserTwAPI(username, "keys")
        str1 =status+username+" Twitter Fetch Success!!"
        if status == "success!":
            video_api.process_img(username)
            video_api.toVideo(username)
            str1 = str1 +"\n Generate Video Finished!!!"
    return str1


@application.route('/feed')
def show_user_profile():
    # show the user video for that user
    account_name = request.args.get('account_name')
    str1 = call_twt_api(account_name)
    video_link = "../static/tweetVideo"+account_name+".mp4"
    return render_template('twitter_feed.html',account_name=account_name,str1 = str1, video_link=video_link)

@application.route('/')
def index():
    return render_template('index.html')


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
