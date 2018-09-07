from datetime import datetime
from flask import  url_for
from werkzeug.utils import redirect
from . import db
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.column()