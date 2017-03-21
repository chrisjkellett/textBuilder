from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired('Please add your email log'),
                                             Email('Incorrect format')])
    password = PasswordField('password', validators=[DataRequired('Please add your password log')])
    login = SubmitField('login')


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[DataRequired('Please add your email reg'),
                                             Email('Incorrect format')])
    password = PasswordField('password', validators=[DataRequired('Please add your password reg'),
                                                     Length(6, 25, 'Incorrect length'),
                                                     EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('repeat password')
    register = SubmitField('register')


class GetText(FlaskForm):
    user_text = TextAreaField('add text', validators=[DataRequired('Please add your text')])