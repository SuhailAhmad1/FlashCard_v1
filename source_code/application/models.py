from re import T
from application.database import db

class User(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String, primary_key = True)
    password = db.Column(db.String, nullable = False)
    
class Deck(db.Model):
    __tablename__ = 'decks'
    deck_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    user = db.Column(db.String, db.ForeignKey("users.username"))
    deck_name = db.Column(db.String, nullable = False)

class Question(db.Model):
    __tablename__ = "questions"
    q_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    deck = db.Column(db.Integer, db.ForeignKey("decks.deck_id"))
    qstn = db.Column(db.String, nullable = False)
    ans = db.Column(db.String, nullable = False)

