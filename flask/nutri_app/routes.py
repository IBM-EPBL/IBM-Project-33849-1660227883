from nutri_app import app
from flask import render_template
@app.route('/')
@app.route('/home')
def homepage():
    return  render_template('homepage.html',title='Home')

@app.route('/about')
def about():
    return  render_template('about.html',title='About')

@app.route('/login')
def login():
    return  render_template('login.html',title='login')
@app.route('/signup')
def signup():
    return  render_template('signup.html',title='signup')
@app.route('/contact')
def contact():
    return  render_template('contact.html',title='contact')



