from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')


class PromotionForm(FlaskForm):
    post = StringField('Title', validators=[Required()])
    body = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')


class PickForm(FlaskForm):
    post = StringField('Title', validators=[Required()])
    body = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')


class ProductionForm(FlaskForm):
    post = StringField('Title', validators=[Required()])
    body = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')


class InterviewForm(FlaskForm):
    post = StringField('Title', validators=[Required()])
    body = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')


class PromotionCommentForm(FlaskForm):
    comment = StringField('Comment: ', validators=[Required()])
    submit = SubmitField('Submit')


class PickCommentForm(FlaskForm):
    comment = StringField('Comment:', validators=[Required()])
    submit = SubmitField('Submit')


class ProductionCommentForm(FlaskForm):
    comment = StringField('Comment: ', validators=[Required()])
    submit = SubmitField('Submit')


class InterviewCommentForm(FlaskForm):
    comment = StringField('Comment: ', validators=[Required()])
    submit = SubmitField('Submit')
