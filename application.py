from flask import Flask
import getUserTweet2Img as twitter_api
import tweetImg2Video as video_api
from markupsafe import escape
from flask import render_template
from flask import request

# EB looks for an 'application' callable by default.
application = Flask(__name__, static_folder='static')


# print a nice greeting.
def say_hello(username=""):
    str = ""
    if username != "":
        str = "The Twitter account name is %s!" % username
        call_twt_api(username)
    return '<p> Welcome to Twitter Feed API!!! \n</p><p>' + str + '</p>\n'


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
    # show the user profile for that user
    account_name = request.args.get('account_name')
    str1 = call_twt_api(account_name)
    video_link = "../static/tweetVideo"+account_name+".mp4"
    return render_template('twitter_feed.html',account_name=account_name,str1 = str1, video_link=video_link)

@application.route('/')
def index():
    return render_template('index.html')

# # some bits of text for the page.
# header_text = '''
#     <html>\n<head> <title>Twitter Feed API</title> </head>\n<body>'''
# instructions = '''
#     <p><em>Hint</em>: This is a RESTful web service!</p><p>\n Append a Twitter Account Name
#     to the URL (for example: <code>/@AnimalPlanet</code>) to call the twitter feed API.</p>\n'''
# home_link = '<p><a href="/">Back</a></p>\n'
# footer_text = '</body>\n</html>'
#
# # add a rule for the index page.
# app.add_url_rule('/', '', (lambda: header_text +
#                                            say_hello() + instructions + footer_text))
#
# # add a rule when the page is accessed with a name appended to the site
# # URL.
# app.add_url_rule('/<username>', 'hello', (lambda username:
#                                                   header_text + say_hello(username) + home_link + footer_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
