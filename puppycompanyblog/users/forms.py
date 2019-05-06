from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from puppycompanyblog.models import User

class LogInForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    username = StringField('UserName', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='password must be matched!')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_email(self, field):
        if (User.query.filter_by(email=field.data).first()):
            raise validationError('Your email have been registered already!')

    def check_username(self, field):
        if (User.query.filter_by(username=field.data).first()):
            raise validationError('Your username has been registered already!')

class UpdateUserForm(FlaskForm):
    username = StringField('UserName', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update profile picture',validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def check_email(self, field):
        if (User.query.filter_by(email=field.data).first()):
            raise validationError('Your email have been registered already!')

    def check_username(self, field):
        if (User.query.filter_by(username=field.data).first()):
            raise validationError('Your username has been registered already!')