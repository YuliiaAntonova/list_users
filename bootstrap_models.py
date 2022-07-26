import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://yaxkxzjufavypv:a204c1f0f3d81bd1ce13e27d7d17c3e08b0b208661d9a98b6b9fd53bc8cc7904@ec2-52-49-120-150.eu-west-1.compute.amazonaws.com:5432/dabjf6hd6mfu3a'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    age = db.Column(db.Integer, index=True)
    address = db.Column(db.String(256))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120), index=True)

db.create_all()


@app.route('/')
def index():
    users = User.query
    return render_template('bootstrap_table.html', title='Bootstrap Table',
                           users=users)


if __name__ == '__main__':
    app.run()
