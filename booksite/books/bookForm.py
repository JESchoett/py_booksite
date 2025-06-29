from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, IntegerField, FloatField, DateField
from wtforms.validators import DataRequired, Optional

class BookForm(FlaskForm):
    autor = StringField(label='Autor', validators=[DataRequired()])
    titel = StringField(label='Titel', validators=[DataRequired()])
    genre = StringField(label='Genre', validators=[Optional()])
    subgenreRomane = StringField(label='Subgenre Romane', validators=[Optional()])
    format = StringField(label='Format', validators=[Optional()])
    verlag = StringField(label='Verlag', validators=[Optional()])
    seiten = IntegerField(label='Seiten', validators=[Optional()])
    isbn = StringField(label='ISBN', validators=[Optional()])
    jahr = IntegerField(label='Jahr', validators=[Optional()])
    preis = FloatField(label='Preis', validators=[Optional()])
    standort = StringField(label='Standort', validators=[Optional()])
    inhaltsangabe = StringField(label='Inhaltsangabe', validators=[Optional()])
    bemerkungen = StringField(label='Bemerkungen', validators=[Optional()])
    subtitel = StringField(label='Subtitel', validators=[Optional()])
    subgenreSachbuchRatgeber = StringField(label='Subgenre Sachbuch/Ratgeber', validators=[Optional()])
    subgenreRatgeber = StringField(label='Subgenre Ratgeber', validators=[Optional()])
    auflage = IntegerField(label='Auflage', validators=[Optional()])
    schlagw = StringField(label='Schlagw', validators=[Optional()])
    bildName = StringField(label='Bild', validators=[Optional()])
    bildCoverInput = FileField('Cover hochladen', validators=[
        Optional(), FileAllowed(['jpg', 'jpeg', 'png'], 'Nur Bilddateien!')
    ])
    submit = SubmitField(label='Submit')
