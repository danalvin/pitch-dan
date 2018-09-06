from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))


class Pitch:
    def __init__(self,id,title,category):
        self.id = id
        self.title = title
        self.category = category


class Comment(db.model):
    __tablename__ = 'reviews'

    id = db.column(db.Integer,primary_key = True)
    pitch_id = db.column(db.Integer)
    pitch_title = db.column(db.string)
    pitch_category = db.column(db.string)
    posted = db.column(db.DateTime,default=datetime.utcnow)
    user_id = db.column(db.Integer,db.ForeignKey("users.id"))


    def save_comments(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
            reviews = Comment.query.filter_by(movie_id=id).all()
            return reviews

            
class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))
    reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")
