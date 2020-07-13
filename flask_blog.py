from flask import Flask
app = Flask(__name__)

'''
Powershell syntax for environment variable
$env:FLASK_APP = "flask_blog.py"
'''

# Basically the root page of the home page
@app.route('/')
def hello_world():
    return 'Hello, World!'

