from flask import render_template, url_for, flash, redirect
from flask_blog import app, db, bcrypt
from flask_blog.forms import RegistrationForm, LoginForm
from flask_blog.models import User, Post


# Dummy data
posts = [
    {
        'author':'Nick Wakefield',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted': '2020-07-13'
    },
    {
        'author':'Jane Doe',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted': '2020-08-01'
    }
]


# Basically the root page of the home page
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)

# Create an about page
@app.route('/about')
def about():
    return render_template('about.html', title = "About")

# Create Register and Login pages
@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!  You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = "Register", form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccesful. Please check username and password', 'danger')
    
    return render_template('login.html', title = "Log In", form = form)
