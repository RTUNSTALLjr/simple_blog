from flask import render_template, redirect, request, session, url_for
from flask_app import app
from flask_app.models import formz
# from flask_app.controllers import review_control

posts = [
    {
    'author' : 'RT',
    'title' : 'post1',
    'content': 'first post',
    'date_posted': 'April 17, 2023'
    },
    {
    'author' : 'BR',
    'title' : 'post2',
    'content': 'second post',
    'date_posted': 'April 17, 2023'
    }
]

@app.route("/")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template("about.html", title = 'About')

@app.route("/register")
def register():
    form = formz.RegistrationForm()
    return render_template("register.html", title = "Register", form = form )

@app.route("/login")
def login():
    form = formz.LoginForm()
    return render_template("login.html", title = "Login", form = form )