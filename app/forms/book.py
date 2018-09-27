"""
    create by misslove
"""
__author__ = 'misslove'

from wtforms import Form,StringField,IntegerField
from wtforms.validators import Length, DataRequired, NumberRange


class SearchForm(Form):
    q = StringField(validators=[DataRequired(message='不能输入空格'), Length(min=1,max=20,message='不能输入空格')])
    page = IntegerField(validators=[NumberRange(min=1,max=99)],default=1)
