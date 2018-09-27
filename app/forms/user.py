"""
    create by misslove
"""
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError, Email, EqualTo
from app.models.user import User

__author__ = 'misslove'


class EmailForm(Form):
    email = StringField(validators=[DataRequired('电子邮箱不可以为空'),Length(
        8,64,message='电子邮箱不符合规范'),Email(message='电子邮箱格式不正确')])

class RegisterForm(EmailForm):

    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请输入你的密码'), Length(6, 32)])

    nickname = StringField(validators=[
        DataRequired(), Length(2, 10, message='昵称至少需要两个字符，最多10个字符')])

    def validate_email(self, field):
        # db.session.
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已存在')

class LoginForm(EmailForm):
    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请输入你的密码'), Length(
            6, 32,message='密码位数输入有误!')])

class ResetPassword(Form):
    password1 = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请输入你的密码'), Length(
            6, 32, message='密码位数输入有误!'),
        EqualTo('password2',message='两次密码输入不一致哦')])
    password2 = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请输入你的密码'), Length(
            6, 32, message='密码位数输入有误!')])