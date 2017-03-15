import time
import hashlib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/textbuilder'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(32))
    active = db.Column(db.Boolean())
    token = db.Column(db.String(32))

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.active = False
        self.token = hashlib.md5(str(time.time()).encode('utf-8')).hexdigest()

    def __repr__(self):
        return '<User %r>' % self.email

