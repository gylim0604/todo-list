from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from app.models import Item

class AddItemForm(FlaskForm):
    body = StringField(default='item...',validators=[DataRequired()])
    checked=1
    submit = SubmitField('Add :D')