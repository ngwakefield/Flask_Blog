'''
Notes:
Powershell syntax for environment variable
$env:FLASK_APP = "flask_blog.py"
Remove the variable by doing Remove-Item Env:\FLASK_APP
Terminal syntax
set VARNAME = SOMETHING
Use setx to make permanent
ctrl-C to end webserver

Database created from command line
Open python, from flask_blog import db
db.create_all()

If python calls this file directly, this will run
Don't need env variable
'''

# This variable (app) has to exist in __init__.py
from flask_blog import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug = True)