from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField, SelectField
from wtforms.validators import InputRequired, NumberRange, Optional, URL


class AddPetForm(FlaskForm):
    name = StringField('Pet name',
                       validators=[InputRequired()])
    species = SelectField('Pet species',
                          choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = TextAreaField('Image URL',
                          validators=[Optional(), URL()])
    age = IntegerField('Age of pet',
                       validators=[NumberRange(min=0, max=30)])  
    notes = TextAreaField('Any notes about this pet.',
                          validators=[Optional()])
    available = BooleanField('Available?')


class EditPetForm(FlaskForm):
    photo_url = TextAreaField('Image URL',
                          validators=[Optional(), URL()])
    notes = TextAreaField('Any notes about this pet.',
                          validators=[Optional()])    
    available = BooleanField('Available?')                     