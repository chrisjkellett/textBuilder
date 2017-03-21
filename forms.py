from flask import Markup
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo


#message variables
noEmailMessage = Markup('Add your <strong>email address</strong>.')
formatEmailMessage = Markup('Incorrect format for <strong>email address</strong>.')
passwordMessage = Markup('Add your <strong>password</strong>.')
passwordLengthMessage = Markup('Passwords must contain at least <strong>6 characters</strong>.')
passwordEqualMessage = Markup('Both <strong>passwords</strong> must match.')


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(noEmailMessage),
                                             Email(formatEmailMessage)])
    password = PasswordField('password', validators=[DataRequired(passwordMessage)])
    login = SubmitField('login')


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(noEmailMessage),
                                             Email(formatEmailMessage)])
    password = PasswordField('password', validators=[DataRequired(passwordMessage),
                                                     Length(6, 25, passwordLengthMessage),
                                                     EqualTo('password2', message=passwordEqualMessage)])
    password2 = PasswordField('repeat password')
    register = SubmitField('register')


class GetText(FlaskForm):
    user_text = TextAreaField('add text', validators=[DataRequired('Please add your text')])