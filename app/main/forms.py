from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required


class PitchForm(FlaskForm):
    category_id = SelectField('Pick A Category', choices=[('1', 'Promotions'), ('2', 'Product'), ('3', 'Interview'), ('4', ('Pickup Lines'), ('5', 'Sales'))])
    comment = TextAreaField('Comments')
    submit = SubmitField('Submit Commennt')

