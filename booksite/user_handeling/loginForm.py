from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField(label='Nutzername', validators=[DataRequired()])
    password = PasswordField(label='Passwort', validators=[DataRequired()])
    submit = SubmitField(label="Einloggen")