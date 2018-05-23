from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required

#Pitch Form
class PitchForm(FlaskForm):
    category_id = SelectField('Pick A Category', choices=[('1', 'Promotions'), ('2', 'Product'), ('3', 'Interview'), ('4', ('Pickup Lines'), ('5', 'Sales'))])
    comment = TextAreaField('Comments')
    submit = SubmitField('Submit Commennt')

#Comment Form
class CommentForm():
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField()
    vote=RadioField('default field arguments', choices=[('1', 'UpVote'), ('1', 'DownVote')])