from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError

class TransactionForm(FlaskForm):
  user_id = IntegerField('user_id', validators=[DataRequired()])
  specialist_id = IntegerField('specialist_id', validators=[DataRequired()])
