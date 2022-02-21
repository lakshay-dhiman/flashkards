from flask import Flask
from flask_restful import Resource, Api
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
app.config['SECRET_KEY'] = 'sakujotitla'


from app.database import db



db.init_app(app)
app.app_context().push()


#api thingy
api = Api(app)
from app.api import AddCard, AddDeck, DeleteDeck, Logout, Register,Login, ReturnCards, ReturnDeckOwner, ReturnDecks, Review
api.add_resource(Register,'/api/register')
api.add_resource(Login,'/api/login')
api.add_resource(AddDeck,'/api/add/deck')
api.add_resource(ReturnDecks,'/api/get/decks')
api.add_resource(AddCard,'/api/add/card')
api.add_resource(ReturnDeckOwner,'/api/get/deckowner')
api.add_resource(ReturnCards,'/api/get/cards')
api.add_resource(Review,'/api/put/review')
api.add_resource(DeleteDeck,'/api/delete/deck')
api.add_resource(Logout,'/api/user/logout')





from app.controler import *

if __name__ == '__main__':
    app.run(debug=True,host = '127.0.0.1',port = 8080)