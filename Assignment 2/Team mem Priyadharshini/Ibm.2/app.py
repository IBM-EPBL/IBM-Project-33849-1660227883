from flask import Flask, render_template, url_for
app = Flask(_name_)

app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def registration():
    return render_template('registration.html')

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/')
def home():
    return render_template('home.html')

if _name_ == '_main_' :
     app.run(debug=True)
