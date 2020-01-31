from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField


class AddPetForm(FlaskForm):
    name = StringField('Pet name')
    species = StringField('Pet species')
    age = IntegerField('Age of pet')
    notes = TextAreaField('Any notes about this pet.')
    available = BooleanField('Available?')
