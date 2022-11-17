from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY']='nutriapp123'
from nutri_app import routes


