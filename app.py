from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

from project.api import api_caller

app = Flask(__name__)


@app.route('/')
def home():
    """
    Home page from the app, root URL.
    :return:
    """
    return render_template('home.html')

@app.route('/search', methods=['POST',])
def search():
    """
    Search method caller, querying in twitter api to fetch data.
    :return:
    """
    inputed_data = request.form.get('hashtag')
    if not inputed_data:
        return redirect('/')
    hashtag = inputed_data if inputed_data.startswith('#')\
        else f'#{inputed_data}'
    tweets = api_caller(hashtag)
    return render_template('result.html',
                           hashtag=hashtag,
                           tweets=tweets.json().get('statuses'))

@app.route('/confirm', methods=['POST',])
def approve():
    """
    Confirmation method where asks the user to confirm and validated
    the selected option
    :return:
    """
    data = request.form.get('selected_tweet')
    name, user, tweet = data.split(';/')
    return render_template('confirm.html',
                           name=name,
                           user=user,
                           tweet=tweet)

@app.route('/approved', methods=['POST', 'GET'])
def approved():
    """
    Method where the approved choice comes, in this test app we simple show
    to the user a thanks message, but in production usage you can modify
    this method to make a request and send data to another endpoint.
    You would need to change the parameter received in this route.
    :return:
    """
    confirmed = request.form.get('confirm')
    if not confirmed:
        return redirect('/')
    return render_template('approved.html')


if __name__ == '__main__':
    app.run(debug=True)
