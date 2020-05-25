from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

from project.api import api_caller

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['POST',])
def search():
    inputed_data = request.form.get('hashtag')
    if not inputed_data:
        return redirect('/')
    hashtag = inputed_data if inputed_data.startswith('#')\
        else f'#{inputed_data}'
    tweets = api_caller(hashtag)
    return render_template('result.html',
                           hashtag=hashtag,
                           tweets=tweets.get('statuses'))

@app.route('/confirm', methods=['POST',])
def approve():
    data = request.form.get('selected_tweet')
    name, user, tweet = data.split(';/')
    return render_template('confirm.html',
                           name=name,
                           user=user,
                           tweet=tweet)

@app.route('/approved', methods=['POST', 'GET'])
def approved():
    confirmed = request.form.get('confirm')
    if not confirmed:
        return redirect('/')
    return render_template('approved.html')


if __name__ == '__main__':
    app.run(debug=True)
