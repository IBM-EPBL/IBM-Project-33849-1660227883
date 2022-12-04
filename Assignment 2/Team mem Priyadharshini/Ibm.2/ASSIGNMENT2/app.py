from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/registration')
def Registration():
    return render_template('registration.html')
@app.route('/home')
def Home():
    return render_template('Home.html')

if __name__ =='__main__':
    app.run(debug=True)



