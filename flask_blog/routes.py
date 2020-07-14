from flask import render_template, url_for, flash, redirect, request
from flask_blog import app, db, bcrypt
from flask_blog.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flask_blog.models import User, Post
from flask_login import login_user, logout_user, current_user, login_required
import secrets
import os

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        # Get the user email from the form
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # Log the user in
            login_user(user, remember = form.remember.data)
            # Get next param from the URL
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
        else:
            flash('Login Unsuccesful. Please check email and password', 'danger')
    
    return render_template('login.html', title = "Log In", form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

def save_picture(form_picture):
    '''
    Pass form_picture as the file object
    '''
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex+f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    form_picture.save(picture_path)
    return picture_fn


@app.route('/account', methods = ['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename = 'profile_pics/'+current_user.image_file)
    return render_template('account.html', title = "Account", 
        image_file = image_file, form = form)