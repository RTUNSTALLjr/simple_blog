from flask import render_template, redirect, request, session, url_for, flash
from flask_app import app, db, bcrypt
from flask_app.models import formz, model
from flask_login import login_user, current_user, logout_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = formz.RegistrationForm()
    print(form)
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = model.User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title = "Register", form = form )

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = formz.LoginForm()
    if form.validate_on_submit():
        user = model.User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Failed. Please check email and password', 'danger')
    return render_template("login.html", title = "Login", form = form )

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html', title = 'Account')