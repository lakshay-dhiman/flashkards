from os import replace
from flask_restful import Resource
from flask import request,redirect,session, render_template
from flask_restful import reqparse
from flask.helpers import flash
from flask_sqlalchemy import _record_queries
from requests.api import delete
from sqlalchemy.util.langhelpers import portable_instancemethod
from werkzeug.security import check_password_hash, generate_password_hash
from flask import current_app as app
from flask_login import login_manager, login_user, current_user,LoginManager, logout_user

from .models import  Cards, Decks, Users
from .database import db

import datetime

login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

user_post_args = reqparse.RequestParser()
user_post_args.add_argument('username')
user_post_args.add_argument('password')

deck_add_post_args = reqparse.RequestParser()
deck_add_post_args.add_argument('name')
deck_add_post_args.add_argument('user_id')


card_add_post_args = reqparse.RequestParser()
card_add_post_args.add_argument('front')
card_add_post_args.add_argument('back')
card_add_post_args.add_argument('deck_id')
card_add_post_args.add_argument('user_id')


deck_owner_post_args = reqparse.RequestParser()
deck_owner_post_args.add_argument('deck_id')

cards_get_args = reqparse.RequestParser()
cards_get_args.add_argument('deck_id')

score_post_args = reqparse.RequestParser()
score_post_args .add_argument('score')
score_post_args .add_argument('deck_id')

deck_delete_args = reqparse.RequestParser()
deck_delete_args.add_argument('deck_id')
deck_delete_args.add_argument('user_id')



class Register(Resource):
    def post(self):

        #post variables
        args = user_post_args.parse_args()

        #length constraint
        if len(args['username']) < 6:
            flash('Username is too short.', category='error')
            return redirect('/register')
        elif len(args['password']) < 6:
            flash('Password is too short.', category='error')
            return redirect('/register')

        #user instance check
        user = Users.query.filter_by(username = args['username']).first()

        if not user:
            new_user = Users(username = args['username'], password=generate_password_hash(args['password'], method='sha256'))
            # try:
                #success
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect('/decks') 
            # except:
            #     # unknown error
            #     flash('An error occured', category='error')
            #     return redirect('/register')
        else:
            #username taken
            flash('Username is already in use.', category='error')
            return redirect('/register')
    
class Login(Resource):
    def post(self):
        #taking parameters
        args = user_post_args.parse_args()

        #checking user instance
        user = Users.query.filter_by(username = args['username']).first()

        if user:
            if check_password_hash(user.password,args['password']):
                login_user(user)
                #success
                return redirect('/decks')
            else:
                flash('Password not correct', category='error')
                return redirect('/login')
        else:
                flash('user not found', category='error')
                return redirect('/login')

class AddDeck(Resource):
    def post(self):
        args = deck_add_post_args.parse_args()
        exists = Decks.query.filter_by(name = args['name']).first()
        if args['name'] == '':
            return 'Name cannot be empty'
        if exists:
            return 'Name cannot be duplicate'
        else:
            new = Decks(name = args['name'],user_id = args['user_id'])
        try:
            db.session.add(new)
            db.session.commit()
            return 'success'
        except:
            return 'an error occured'


class ReturnDecks(Resource):
    def get(self):
        decks_init = Decks.query.all()
        decks = []
        
        for deck in decks_init:
            user = Users.query.filter_by(id = deck.user_id).first()
            if(deck.count!=0):
                final_score = "{:.2f}".format(deck.score/deck.count)
            else:
                final_score = 0
            s= ''
            date_now_arr = ([deck.last_rev.strftime('%d'),'-',deck.last_rev.strftime('%m'),'-',deck.last_rev.strftime('%G'),' | ',deck.last_rev.strftime('%H'),':',deck.last_rev.strftime('%M')])
            date_now_final= s.join(date_now_arr)
            decks.append([deck.id,deck.name,user.username,date_now_final,deck.user_id,final_score])
        return decks

class AddCard(Resource):
    def post(self):
        args = card_add_post_args.parse_args()
        deck_search = Decks.query.filter_by(id=args['deck_id']).first()
        if(args['front'] == '' or args['back'] == ''):
            return 'Fields cannot be empty'
        if int(deck_search.user_id) == int(args['user_id']) :
            new_card = Cards(front = args['front'], back = args['back'], deck_id = args['deck_id'])
            try:
                db.session.add(new_card)
                db.session.commit()
                return "success"
            except:
                return 'something went wrong'
        else:
            return 'not allowed'

class ReturnDeckOwner(Resource):
    def get(self):
        args = deck_owner_post_args.parse_args()
        deck = Decks.query.filter_by(id = args['deck_id']).first()
        # user_id = deck['username']
        return deck.user_id



class ReturnCards(Resource):
    def get(self):
        args = cards_get_args.parse_args()
        cards_init = Cards.query.filter_by(deck_id = args['deck_id']).all()
        cards = []
        count= 0
        for card in cards_init:
            count += 1
            cards.append([count,card.front,card.back])
        return cards


class Review(Resource):
    def post(self):
        args = score_post_args.parse_args()
        deck_search = Decks.query.filter_by(id=args['deck_id']).first()
        # print(args)
        if deck_search:
            # score_instance = Score.query.filter_by(deck_id = args['deck_id']).first()
            # if not score_instance:
                # first_score = Score(deck_id = args['deck_id'])
                # try:  
                #     db.session.add(first_score)
                #     db.session.commit()
                #     return 'success'
                # except:
                #     return 'error'
            
            # score = Deck.query.filter_by(deck_id = args['deck_id']).first()

            deck_search.score += int(args['score'])
            deck_search.count += 1
            date = datetime.datetime.now()
            # s= ''
            # date_now_arr = ([date.strftime('%d'),'-',date.strftime('%m'),'-',date.strftime('%G'),',',date.strftime('%H'),':',date.strftime('%M')])
            # date_now= s.join(date_now_arr)
            deck_search.last_rev = date
            # try:    
            db.session.commit()
            return 'succcess'
            # except:
                # return 'error'
        return 'no deck'

class DeleteDeck(Resource):
    def delete(self):
        args = deck_delete_args.parse_args()
        deck = Decks.query.filter_by(id = args['deck_id']).first()
        # print(deck.user_id,args['user_id'])
        if int(deck.user_id) == int(args['user_id']):
            db.session.delete(deck)
            db.session.commit()
            return 'success'
        else:
            return 'not authorised'

class Logout(Resource):
    def get(self):
        logout_user()
        return redirect('/')