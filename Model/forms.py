from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField
from wtforms.validators import DataRequired


class ItemForm(FlaskForm):
    item_name = StringField('Item name', validators=[DataRequired()])
    expired_date = DateField('expired date', validators=[DataRequired()])
    use_after_open = IntegerField('expired when opened (days)', validators=[DataRequired()])
    do_i_need_it = IntegerField('do you need it? :) (0-10)', validators=[DataRequired()])
