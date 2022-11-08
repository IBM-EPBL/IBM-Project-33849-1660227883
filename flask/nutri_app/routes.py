from nutri_app import app
from flask import render_template, url_for

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

@app.route('/register')
def register():
    return  render_template('register.html',title='Register')

@app.route('/contact')
def contact():
    return  render_template('contact.html',title='contact')

@app.route('/dashboard')
def dashboard():
    return  render_template('dashboard.html',title='dashboard')



