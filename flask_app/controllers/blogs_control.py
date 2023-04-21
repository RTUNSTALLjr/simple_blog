from flask import render_template, redirect, request, session, url_for, flash
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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = formz.RegistrationForm()
    print(form)
    if form.validate_on_submit():
        print(form.password.data)
        form.password.data = "banana"
        print(form.password.data)
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title = "Register", form = form )

@app.route("/login", methods=["GET", "POST"])
def login():
    form = formz.LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Please check email and password", "danger")
    return render_template("login.html", title = "Login", form = form )