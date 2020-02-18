from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class ItemForm(FlaskForm):
    item_name = StringField('Item name', validators=[DataRequired()])
    expired_date = DateField('expired date', validators=[DataRequired()])
    use_after_open = IntegerField('expired when opened (days)', validators=[DataRequired()])
    do_i_need_it = IntegerField('do you need it? :) (0-10)', validators=[DataRequired()])


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    e_mail = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[EqualTo('password')])
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    e_mail = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign up')