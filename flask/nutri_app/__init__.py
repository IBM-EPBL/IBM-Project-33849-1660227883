from flask import Flask
import ibm_db

app = Flask(__name__)
app.secret_key='1aaa'
app.config['SECRET_KEY']='nutriapp123'
from nutri_app import routes


