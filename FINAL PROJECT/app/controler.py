from flask import Flask,session
from flask import current_app as app
from flask.templating import render_template
from flask.wrappers import Request
from flask_login.utils import login_required
from werkzeug.utils import redirect
from flask_login import LoginManager, current_user
import requests

BASE = 'http://127.0.0.1:8080'

@app.route('/register', methods=['GET'])
def registeration():
    if(current_user.is_authenticated):
        return redirect('/')
    else:
        return render_template('register.html')

@app.route('/login', methods = ['GET'] )
def loginHere():
    if(current_user.is_authenticated):
        return redirect('/')
    else:
        return render_template('login.html')


@app.route('/', methods = ['GET'] )
def home():
    if current_user.is_authenticated:
        return redirect('/decks')
    else:
        return render_template('home.html')

@login_required
@app.route('/decks', methods = ['GET'])
def decks():
    decks = requests.get(BASE+'/api/get/decks')
    return render_template('decks.html', decks= decks.json())

@login_required
@app.route('/cards/<int:deck_id>')
def cards(deck_id):
    user_id = requests.get(BASE+'/api/get/deckowner', params = {"deck_id" : deck_id})
    cards = requests.get(BASE+'/api/get/cards', params = {'deck_id' : deck_id})
    return render_template('cards.html',user_id = user_id.json(), deck_id= deck_id, cards = cards.json())

