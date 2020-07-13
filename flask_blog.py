from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '0907aeb5e25a61b08f7c15770f467f64'
'''
Powershell syntax for environment variable
$env:FLASK_APP = "flask_blog.py"

ctrl-C to end webserver
'''
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
def hello_world():
    return render_template('home.html', posts = posts)

# Create an about page
@app.route('/about')
def about():
    return render_template('about.html', title = "About")

# Create Register and Login pages
@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title = "Register", form = form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = "Log In", form = form)

# If python calls this file directly, this will run
# Don't need env variable
if __name__ == '__main__':
    app.run(debug = True)