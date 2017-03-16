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
    save_text = db.relationship('Savetext', backref='user', lazy='dynamic')

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.active = False
        self.token = hashlib.md5(str(time.time()).encode('utf-8')).hexdigest()

    def __repr__(self):
        return '<User %r>' % self.email


class Savetext(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    gettext = db.Column(db.String(5000))
    id_user = db.Column(db.ForeignKey('user.id'))

    def __init__(self, name, gettext, id_user):
        self.name = name
        self.gettext = gettext
        self.id_user = id_user

    def __repr__(self):
        return '<Savetext %r>' % self.name