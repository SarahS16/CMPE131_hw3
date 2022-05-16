from flask import Flask
myapp = Flask(__name__)
myapp.secret_key = b'_3L#4E3\n\xec'
from app import routes