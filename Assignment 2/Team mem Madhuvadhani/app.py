from flask import Flask, render_template


app=Flask(__name__)

@app.route('/index')
def index():
    return render_template('Index.html')


@app.route('/home')
def home():
    return render_template('Home page.html')

@app.route('/login')
def login():
    return render_template('Login page.html')

@app.route('/register')
def register():
    return render_template('Registeration page.html')






if __name__=='__main__':
    app.run()
