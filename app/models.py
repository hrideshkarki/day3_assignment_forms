from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
import requests

db = SQLAlchemy()

class Pokemon:
    def __init__(self, name):
        self.name = name
        self.data = self._get_pokemon_data(name)

    def _get_pokemon_data(self, name):
        url = f'https://pokeapi.co/api/v2/pokemon/{name}'
        response = requests.get(url)
        data = response.json()
        return data

    def get_image_url(self):
        return self.data["sprites"]["front_shiny"]

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), nullable = False)
    last_name = db.Column(db.String(45), nullable = False)
    username = db.Column(db.String(45), nullable = False, unique = True)
    email = db.Column(db.String(100), nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)
    date_created = db.Column(db.DateTime, nullable = False, default=datetime.utcnow())

    def __init__(self, first_name, last_name, username, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable = False)
#     img_url = db.Column(db.String, nullable = False)
#     caption = db.Column(db.String(500))
#     date_created = db.Column(db.DateTime, nullable = False, default=datetime.utcnow())
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

#     def __init__(self, title, img_url, caption, user_id):
#         self.title = title
#         self.img_url = img_url
#         self.caption = caption
#         self.user_id = user_id

#     def saveToDB(self):
#         db.session.add(self)
#         db.session.commit()