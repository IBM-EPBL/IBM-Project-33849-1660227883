from flask import Flask
import requests
from flask_mail import Mail,Message

app = Flask(__name__)



from nutri_app import routes
