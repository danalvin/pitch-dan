from datetime import datetime
from flask import  url_for
from werkzeug.utils import redirect
from . import db
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    promotion = db.relationship('Promotion', backref='user', lazy='dynamic')
    pick = db.relationship('Pick', backref='user', lazy='dynamic')
    production = db.relationship('Production', backref='user', lazy='dynamic')
    interview = db.relationship('Interview', backref='user', lazy='dynamic')
    promocomments = db.relationship('CommentsPromotion', backref='user', lazy='dynamic')
    pickcomments = db.relationship('CommentsPick', backref='user', lazy='dynamic')
    producomments = db.relationship('CommentsProduction', backref='user', lazy='dynamic')
    intcomments = db.relationship('CommentsInterview', backref='user', lazy='dynamic')
    like = db.relationship('Like', backref='user', lazy='dynamic')
    unlike = db.relationship('Unlike', backref='user', lazy='dynamic')

       def __repr__(self):
        return f'User{self.username}'

    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


class Pick(db.Model):
    __tablename__ = 'pick'
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(255))
    body = db.Column(db.String(1000))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_pick(self):
        db.session.add(self)
        db.session.commit()


class CommentsPick(db.Model):
    __tablename__ = 'commentspick'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    pick_id = db.Column(db.Integer, db.ForeignKey("pick.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_pick_coments(self):
        db.session.add(self)
        db.session.commit()


class Promotion(db.Model):
    __tablename__ = 'promotion'
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(255))
    body = db.Column(db.String(1000))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment = db.relationship('CommentsPromotion', backref='promotion', lazy='dynamic')

    def save_promotion(self):
        db.session.add(self)
        db.session.commit()


class CommentsPromotion(db.Model):
    __tablename__ = 'commentspromotion'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    promotion_id = db.Column(db.Integer, db.ForeignKey("promotion.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_promo_coments(self):
        db.session.add(self)
        db.session.commit()


class Production(db.Model):
    __tablename__ = 'production'
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(255))
    body = db.Column(db.String(1000))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_production(self):
        db.session.add(self)
        db.session.commit()


class CommentsProduction(db.Model):
    __tablename__ = 'commentsproduction'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    production_id = db.Column(db.Integer, db.ForeignKey("production.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_produ_coments(self):
        db.session.add(self)
        db.session.commit()


class Interview(db.Model):
    __tablename__ = 'interview'
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(255))
    body = db.Column(db.String(1000))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_production(self):
        db.session.add(self)
        db.session.commit()


class CommentsInterview(db.Model):
    __tablename__ = 'commentsinterview'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    interview_id = db.Column(db.Integer, db.ForeignKey("interview.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_int_coments(self):
        db.session.add(self)
        db.session.commit()


class Like(db.Model):
    __tablename__ = 'likes'
    id = db.Column(db.Integer, primary_key=True)
    like = db.Column(db.Integer, default=1)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_like(self):
        db.session.add(self)
        db.session.commit()


class Unlike(db.Model):
    __tablename__ = 'unlikes'
    id = db.Column(db.Integer, primary_key=True)
    unlike = db.Column(db.Integer, default=1)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_unlike(self):
        db.session.add(self)
        db.session.commit()
