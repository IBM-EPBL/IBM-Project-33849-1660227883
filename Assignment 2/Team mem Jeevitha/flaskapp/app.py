from flask impport flask,render,template


app=flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('Home page.html')

@app.route('/login')
def login():
    return render_template('Login page.html')

@app.route('/regiser')
def register():
    return render_template('Registeration page.html')






    if __name__=='main':
        app.run()    
