from flask import Flask
from flask_wtf import CSRFProtect
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


from commands import *
