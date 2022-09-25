

from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/registration')
def Registration():
    return render_template('Registration.html')
@app.route('/signup')
def SignUp():
    return render_template('Signup.html')
@app.route('/home')
def Home():
    return render_template('Home.html')
