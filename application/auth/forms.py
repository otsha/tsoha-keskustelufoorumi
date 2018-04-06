from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

# Define the login form
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

# Define the register form
class RegisterForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=3)])
    password = PasswordField("Password", [validators.Length(min=4)])

    class Meta:
        csrf = False