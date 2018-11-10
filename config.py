from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from rq import Queue
from worker import conn


app = Flask(__name__)
app.config['SECRET_KEY'] = 'UNKNOWNSECRETKEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///edyst.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
q = Queue(connection=conn)

from views import *