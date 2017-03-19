from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class Login_form(FlaskForm):
    email = StringField('email')
    password = PasswordField('password')
    login = SubmitField('login')


class Register_form(FlaskForm):
    email = StringField('email', validators=[DataRequired('Please add your username'),
                                             Email('Incorrect format'),
                                             Length(1, 80, 'Incorrect length')])
    password1 = PasswordField('password', validators=[DataRequired('Please add your password'),
                                                      Length(6, 25, 'Incorrect length')])
    password2 = PasswordField('repeat password', validators=[DataRequired('Please add your password again')])
    register = SubmitField('register')


class getText(FlaskForm):
    user_text = TextAreaField('add text', validators=[DataRequired('Please add your text')])