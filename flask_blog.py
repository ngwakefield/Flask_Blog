from flask import Flask
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
    return '<h1> Hello, World! I am running Flask. </h1>'

# Create an about page
@app.route('/about')
def about():
    return '<h1> About Page. </h1>'


# If python calls this file directly, this will run
# Don't need env variable
if __name__ == '__main__':
    app.run(debug = True)