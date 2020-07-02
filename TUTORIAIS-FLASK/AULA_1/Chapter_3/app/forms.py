from flask_wtf import FlaskForm    # Importing flask_wtf module
from wtforms import StringField, PasswordField, BooleanField, SubmitField  # Importing the fields used to create the HTML impus
from wtforms.validators import DataRequired # Data required is an alert informing a must input on Login form


class LoginForm(FlaskForm):   # It's a class based Form, to created the required fields

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
