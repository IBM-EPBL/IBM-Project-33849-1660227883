
from nutri_app import app
from flask import render_template, url_for, request, redirect, session
from nutri_app.forms import RegistrationForm,LoginForm
# from flask_mail import Mail,Message
import requests
import re

import ibm_db
try:
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=fbd88901-ebdb-4a4f-a32e-9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32731;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=bsb24991;PWD=IFwF1CIR5TduWOx7",'','')
except Exception as e:
    print(e)


# mail = Mail(app)

# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'anuani12@gmail.com'
# app.config['MAIL_PASSWORD'] = 'aag'
# app.config['MAIL_USE_TLS']  = False
# app.config['MAIL_USE_SSL'] = True

# mail = Mail(app)




@app.route('/index')
def index():
    return render_template("index.html")

# @app.route('/result',methods=['POST','GET'])
# def result():
#      if request.method == "POST":
#          msg = Message(request.form.get("Subject"),sender='anuani191312@gmail.com', recipients=[request.form.get("Email")])
#          msg.body = "cool mail bro"
#          mail.send(msg)
#          return render_template('result.html',result="success!")
#      else:
#          return render_template('result.html', result="failure!")

@app.route('/')
@app.route('/home')
def homepage():
    return  render_template('homepage.html',title='Home')

@app.route('/about')
def about():
    return  render_template('about.html',title='About')

@app.route("/signin")
def signin():
    return render_template("login1.html")
        

@app.route('/login',methods =['GET', 'POST'])
def login():
    global userid
    msg = ''
   
    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['password']
        query = "SELECT * FROM register WHERE username = ? AND password = ?;"
        stmt = ibm_db.prepare(conn,query)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_tuple(stmt)
        print (account)
        
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            userid=  account[0]
            session['username'] = account[1]
           
            return redirect(url_for('dashboard'))
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)

# def login():
#     if p:
#         if form.email.data=='anuani191312@gmail.com' and form.password.data=='anuani123':
#             return redirect(url_for('dashboard'))
#         else:
#             return redirect(url_for('homepage'))
#     return  render_template('login.html',title='login',form=form)

# @app.route('/register',methods=['POST','GET'])
# def register():
#     form=RegistrationForm()
#     if form.validate_on_submit():
#         return redirect(url_for('add'))
#     return  render_template('register.html',title='register',form=form)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' :
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['cpassword']
        query = 'SELECT * FROM register WHERE username =?;'
        stmt=ibm_db.prepare(conn,query)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'name must contain only characters and numbers !'
        elif password != cpassword:
            msg = "password doesn't match"
        else:
            query = "INSERT INTO register (username,password,email) VALUES (?,?,?)"
            stmt=ibm_db.prepare(conn,query)
            ibm_db.bind_param(stmt,1,username)
            ibm_db.bind_param(stmt,2,password)
            ibm_db.bind_param(stmt,3,email)
            ibm_db.execute(stmt)
            msg = 'You have successfully registered !'
    return render_template('signup.html', msg = msg)


@app.route('/contact')
def contact():
    return  render_template('contact.html',title='contact')
@app.route('/add')
def add():
    return  render_template('add.html',title='add')

@app.route('/dashboard')
def dashboard():
    return  render_template('dashboard.html',title='dashboard')
@app.route('/logout')
def logout():
    return  render_template('logout.html',title='logout')
@app.route('/tqpage')
def tqpage():
    return  render_template('tqpage.html',title='tqpage')
@app.route('/tips')
def tips():
    return  render_template('tips.html',title='tips')
@app.route('/register1',methods=['GET','POST'])
def register1():
    return render_template('register1.html',title='register1')

@app.route('/login1')
def login1():
    return  render_template('login1.html',title='login1')



@app.route('/foodservices')
def foodservices():
    return  render_template('foodservices.html',title='foodservices')

@app.route('/calorietracker')
def calorietracker():
    return  render_template('calorietracker.html',title='calorietracker')

@app.route('/recipes')
def recipes():
    return  render_template('recipes.html',title='recipes')





@app.route('/food', methods=["POST"])
def food():
    if request.method =="POST":
        print(request.form.get("foodservices"))
       

        url = "https://calorieninjas.p.rapidapi.com/v1/nutrition"

        querystring = {"query":request.form.get("food")}

        headers = {
	"X-RapidAPI-Key": "f50dae66d6msh719422f3b99f765p1c60d7jsn3e9c15440173",
	"X-RapidAPI-Host": "calorieninjas.p.rapidapi.com"
}

        response = requests.request("GET", url, headers=headers, params=querystring)
        if(response):
         print(response.json()['items'][0]['calories'])
    return  render_template('foodservices.html',title='logout',name=response.json()['items'][0]['name'],calorie=response.json()['items'][0]['calories']
    ,sugar=response.json()['items'][0]['sugar_g'],fiber=response.json()['items'][0]['fiber_g'], 
    serving_size=response.json()['items'][0]['serving_size_g'],sodium=response.json()['items'][0]['sodium_mg'],potassium=response.json()['items'][0]['potassium_mg'],fat_saturated=response.json()['items'][0]['fat_saturated_g'],
    fat_total=response.json()['items'][0]['fat_total_g'],cholesterol=response.json()['items'][0]['cholesterol_mg'],protein=response.json()['items'][0]['protein_g'],
    carbohydrates_total=response.json()['items'][0]['carbohydrates_total_g'])

