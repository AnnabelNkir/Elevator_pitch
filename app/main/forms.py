from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField

class PitchForm(FlaskForm):

    title = StringField('Pitch title')
    category= SelectField('Pitch Category', choices=[('Select a category', 'Select a category'),('Business', 'Business'),('Science and Tech', 'Science and Tech'),('Interview Pitch', 'Interview Pitch'),('Maths pitch', 'Maths pitch'),('Pick-up lines', 'Pick-up lines')])
    content = TextAreaField('The pitch...')
    submit = SubmitField('Post')
