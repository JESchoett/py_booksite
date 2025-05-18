from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, Optional

class MovieForm(FlaskForm):
    autor = StringField(label='Autor', validators=[DataRequired()])
    titel = StringField(label='Titel', validators=[DataRequired()])
    genre = StringField(label='Genre', default=" ", validators=[Optional()])
    subgenreRomane = StringField(label='Subgenre Romane', default=" ", validators=[Optional()])
    format = StringField(label='Format', default=" ", validators=[Optional()])
    verlag = StringField(label='Verlag', default=" ", validators=[Optional()])
    laenge = StringField(label='Laenge', default=" ", validators=[Optional()])
    isbn = StringField(label='ISBN', default=" ", validators=[Optional()])
    jahr = IntegerField(label='Jahr', default=0, validators=[Optional()])
    preis = FloatField(label='Preis', default=0.0, validators=[Optional()])
    standort = StringField(label='Standort', default=" ", validators=[Optional()])
    inhaltsangabe = StringField(label='Inhaltsangabe', default=" ", validators=[Optional()])
    bemerkungen = StringField(label='Bemerkungen', default=" ", validators=[Optional()])
    subtitel = StringField(label='Subtitel', default=" ", validators=[Optional()])
    subgenreSachbuchRatgeber = StringField(label='Subgenre Sachbuch/Ratgeber', default=" ", validators=[Optional()])
    subgenreRatgeber = StringField(label='Subgenre Ratgeber', default=" ", validators=[Optional()])
    auflage = IntegerField(label='Auflage', default=0, validators=[Optional()])
    schlagw = StringField(label='Schlagw', default=" ", validators=[Optional()])
    bild = StringField(label='Bild', default=" ", validators=[Optional()])
    submit = SubmitField(label='Submit')
