1.project/
│
├── app/
│   ├── models.py         # SQLAlchemy models (User, Discussion, Comment)
│   ├── routes.py         # Flask routes (API endpoints)
│   ├── utils.py          # Utility functions (e.g., for hashing passwords)
│   └── __init__.py       # Initialization of Flask app
│
├── db.sqlite             # SQLite database file
│
└── run.py                # Script to run the Flask app

2.Define SQLAlchemy Models (app/models.py)
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    mobile_no = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

class Discussion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255))  # path to image file
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('discussions', lazy=True))

class Hashtag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

class DiscussionHashtag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    discussion_id = db.Column(db.Integer, db.ForeignKey('discussion.id'))
    hashtag_id = db.Column(db.Integer, db.ForeignKey('hashtag.id'))

3.Initialize Flask App (app/__init__.py)
from flask import Flask
from flask_cors import CORS
from .models import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    CORS(app)  # for cross-origin requests if needed
    return app



4.. Define API Endpoints (app/routes.py)
from flask import jsonify, request, abort
from .models import db, User, Discussion, Hashtag, DiscussionHashtag
from .utils import hash_password

app = create_app()

@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users])

# Implement other routes similar to the above for creating, updating, deleting users,
# searching users by name, etc.

@app.route('/api/discussions', methods=['POST'])
def create_discussion():
    data = request.get_json()
    text = data.get('text')
    image = data.get('image')
    hashtags = data.get('hashtags', [])

    # Example: Creating a discussion
    new_discussion = Discussion(text=text, image=image)
    db

5.








