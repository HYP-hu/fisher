"""
    create by misslove
"""

from wtforms import Form, StringField
from wtforms.validators import DataRequired, Length, Regexp

__author__ = 'misslove'


class DriftForm(Form):
    recipient_name = StringField(
        '收件人姓名',validators=[DataRequired('收件人姓名不能为空'),
                                 Length(min=2,max=20,
                                        message='收件人姓名长度必须在2到20之间')])

    mobile = StringField(
        '手机号',validators=[DataRequired('收件人手机号码不能为空'),
                       Regexp('^1[0-9]{10}$',0,'请输入正确手机号')])

    message = StringField()

    address = StringField(
        '邮寄地址', validators = [DataRequired('邮寄地址不能为空'),
                           Length(min=10,max=70,
                            message='邮寄地址请写详细一些嘛')])
