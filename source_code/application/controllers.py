from flask import render_template
from flask import Flask,request
from flask import current_app as app
from werkzeug.utils import redirect
from application.models import Deck, User, Question
from application.database import db

@app.route("/", methods = ["GET","POST"])
def login():
    return render_template('login.html')

@app.route("/home", methods = ["GET","POST"])
def home():
    n = request.form.get("user")
    p = request.form.get("pass")
    user = db.session.query(User).filter(User.username == n).first()
    if user:
        decks = Deck.query.filter_by(user = n)
        return render_template("home.html",NAME = n,deck = decks)
    else:
        n_user = User(username = n, password = p)
        db.session.add(n_user)
        db.session.commit()
        return render_template("n_home.html",NAME = n)


@app.route("/home/<user>/<deck_id>/<q_n>", methods = ["GET", "POST"])
def in_deck(user=None, deck_id = 0,q_n=0):
    q_n = int(q_n)
    question = Question.query.filter_by(deck = deck_id)
    qs = {}
    for i in range(5):
        qs[i] = question[i].qstn  
    anss = {}
    for i in range(5):
        anss[i] = question[i].ans
    q_n+=1
    return render_template("in_deck.html",question = qs[q_n-1],answer = anss[q_n-1],deck_id = deck_id,q_n = q_n,user_i = user)

@app.route("/create/<user>", methods = ["GET", "POST"])
def create(user):
    return render_template("create.html",NAME = user)

@app.route("/succ_msg/<user>", methods = ["GET", "POST"])
def re_home(user=None):
    decks = Deck.query.filter_by(user = user)
    return render_template("home.html",NAME = user,deck = decks)

@app.route("/created/<user>", methods = ["GET","POST"])
def created(user):
    deck_n = request.form.get("deck_name")
    new_deck = Deck(user = user, deck_name = deck_n)
    db.session.add(new_deck)
    db.session.commit()
    q1 = request.form.get("q1")
    a1 = request.form.get("a1")
    q2 = request.form.get("q2")
    a2 = request.form.get("a2")
    q3 = request.form.get("q3")
    a3 = request.form.get("a3")
    q4 = request.form.get("q4")
    a4 = request.form.get("a4")
    q5 = request.form.get("q5")
    a5 = request.form.get("a5")
    new_q = Question(deck = new_deck.deck_id, qstn = q1, ans = a1)
    db.session.add(new_q)
    db.session.commit()
    new_q = Question(deck = new_deck.deck_id, qstn = q2, ans = a2)
    db.session.add(new_q)
    db.session.commit()
    new_q = Question(deck = new_deck.deck_id, qstn = q3, ans = a3)
    db.session.add(new_q)
    db.session.commit()
    new_q = Question(deck = new_deck.deck_id, qstn = q4, ans = a4)
    db.session.add(new_q)
    db.session.commit()
    new_q = Question(deck = new_deck.deck_id, qstn = q5, ans = a5)
    db.session.add(new_q)
    db.session.commit()
    return render_template("success.html",usr = user,work = "Created")

@app.route("/delete/<user>/<deck_id>",methods = ["GET","POST"])
def delete(user= None,deck_id=0):
    Question.query.filter_by(deck = deck_id).delete()
    deck = db.session.query(Deck).filter(Deck.deck_id == deck_id).first()
    db.session.delete(deck)
    db.session.commit()
    return render_template("success.html",usr = user, work = "Deleted")

@app.route("/<user>/update/<deck_id>/<no>",methods = ["GET","POST"])
def update(user = None, deck_id = 0,no = None):
    n = int(no)
    return render_template("create.html",NAME = user,deck_id = deck_id,check = n)

@app.route("/updated/<user>/<deck_id>", methods = ["GET","POST"])
def updated(user = None,deck_id =0):
    q1 = request.form.get("q1")
    a1 = request.form.get("a1")
    q2 = request.form.get("q2")
    a2 = request.form.get("a2")
    q3 = request.form.get("q3")
    a3 = request.form.get("a3")
    q4 = request.form.get("q4")
    a4 = request.form.get("a4")
    q5 = request.form.get("q5")
    a5 = request.form.get("a5")
    questns = Question.query.filter_by(deck = deck_id)
    print(questns)
    questns[0].qstn = q1
    questns[0].ans = a1
    questns[1].qstn = q2
    questns[1].ans = a2
    questns[2].qstn = q3
    questns[2].ans = a3
    questns[3].qstn = q4
    questns[3].ans = a4
    questns[4].qstn = q5
    questns[4].ans = a5
    db.session.commit()
    return render_template("success.html",usr = user, work = "Updated")