import flask
from flask import request, jsonify

app = flask.Flask(__name__)

#setting information on villagers for API 
villagers = [
    {'id': 0,
     'name': 'Cyrano',
     'birthday': 'March 9th'},
    {'id': 1,
     'name': 'Antonio',
     'birthday': 'October 20th'},
    {'id': 2,
     'name': 'Pango',
     'birthday': 'November 9th'}
]


@app.route('/', methods=['GET']) #defining the home page of the API
def home():
    return '''<h1>ACNH API</h1>
<p>An example of an API made by Melanie Martinez</p>'''


@app.route('/api/v1/acnh/villagers/all', methods=['GET']) #defining the route, and printing the villager info set above
def melanie_api():
    return jsonify(villagers)

app.run()