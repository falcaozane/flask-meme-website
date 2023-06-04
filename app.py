from flask import Flask,redirect,url_for,render_template
import json
import requests

app=Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET",url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large,subreddit

@app.route('/')
def index():
    meme_pic,subreddit = get_meme()
    return render_template('index.html', meme_pic = meme_pic, subreddit = subreddit)

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)