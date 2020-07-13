from flask import Flask, render_template
app = Flask(__name__)

'''
Powershell syntax for environment variable
$env:FLASK_APP = "flask_blog.py"

ctrl-C to end webserver
'''

# Basically the root page of the home page
@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html')

# Create an about page
@app.route('/about')
def about():
    return render_template('about.html')


# If python calls this file directly, this will run
# Don't need env variable
if __name__ == '__main__':
    app.run(debug = True)