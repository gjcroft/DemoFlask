#flask demo app
from flask import Flask, flash, redirect, render_template, request, session, abort
from os import environ
from datetime import datetime
import os


app = Flask(__name__)
app.secret_key = os.urandom(12)
#Main structure some imports above for key modules required

#you basically now make your routes ie your page links either with templates or simply code first few will be code
#then will show how to use a template

@app.route('/') #this is the root of the website basically the home page
#you make a function to handle the route
def home():
    #we will simply return a message in text
    return('Welcome to flask')

#so we can make another route that will return html
@app.route('/html')
def html():
    return('<h1>Welcome to flask with HTML</h1>')

#use get to send a variable (basically how to make api's)
@app.route('/variable/<name>')
def variable(name):
    myname = name
    return('Welcome, '+name)

#returning a template saves writing webpages over and over kind of like a site master
@app.route('/template')
def withtemplate():
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        message = 'This message is passed into the template from the views'
        
    )

#post data from a form
@app.route('/form',methods=['GET','POST'])
def myform():
    if request.method == "POST":
        yourname = request.form['yourname']
        return('you posted your name as : ' + yourname)
    
    else:
        return render_template('myform.html')



#The below code runs the app as a webserver on port 5555 if you open localhost and port 5555 you will see the app
if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000
    app.run(HOST, PORT)