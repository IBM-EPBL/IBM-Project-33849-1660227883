from flask import Flask, render_template, url_for
app = Flask(__name__)

app.route('/index')
def index():
    return render_template('index.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__' :
     app.run(debug=True)


