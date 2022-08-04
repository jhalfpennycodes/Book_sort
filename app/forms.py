from flask_wtf import FlaskForm as Form
from wtforms import StringField, validators, PasswordField, BooleanField, TextAreaField, SelectField


class LoginForm(Form):
    username = StringField('username', validators=[validators.InputRequired(), validators.Length(min=4, max=15)])
    password = PasswordField('password', validators=[validators.InputRequired(), validators.Length(min=6, max=20)])
    remember = BooleanField('remember me')


class RegisterForm(Form):
    username = StringField('username', validators=[validators.InputRequired(), validators.Length(min=4, max=20)])
    password = PasswordField('password', validators=[validators.InputRequired(), validators.Length(min=6, max=20)])
    name = StringField('name')


class Add_book(Form):
    title = StringField('Title', validators=[validators.DataRequired('Title is required')])
    author = StringField('Author', validators=[validators.DataRequired('Author is required')])
    description = TextAreaField('Description')
    rating = SelectField('Rating', choices=[1, 2, 3, 4, 5])