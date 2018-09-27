"""
    create by misslove
"""
from flask import render_template, request, redirect, url_for, flash, current_app
from flask_login import login_user, current_user, logout_user, login_required

from app.forms.user import RegisterForm, LoginForm, EmailForm, ResetPassword
from app.models.base import db
from app.models.user import User

__author__ = 'misslove'
from . import web

@web.route('/register/',methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
        return redirect(url_for('web.login'))
    #form传进去 把form.data的数据和form.errors信息传进去
    return render_template('auth/register.html',form=form)

@web.route('/login/',methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email = form.email.data).first()
        if user and user.check_password(form.password.data):
            current_app.logger.warning(user.nickname+'登录了网站')
            login_user(user)
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账号不存在或密码错误!')
    return render_template('auth/login.html',form=form)

@web.route('/forget/',methods=['GET','POST'])
def forget_password_request():
    form = EmailForm(request.form)
    if request.method=="POST" and form.validate():
        user=User.query.filter_by(email=form.email.data).first_or_404()
        from app.libs.email import  send_mail
        account_email = form.email.data
        send_mail('841191837@qq.com','重置您的密码','email/reset_password.html',
                  user=user,token=user.generate_token())
        flash('一封邮件已发到邮箱'+account_email+'请及时处理')
    return render_template('auth/forget_password_request.html',form=form)

@web.route('/resent/password/<token>',methods=['GET','POST'])
def forget_password(token):
    #重置密码
    form = ResetPassword(request.form)
    if request.method=='POST' and form.validate():
        success = User.reset_password(token,form.password1.data)
        if success:
            flash('密码已经更新,请用新密码登录')
            return redirect(url_for('web.login'))
        flash('密码重置失败')
    return render_template('auth/forget_password.html',form=form)

@web.route('/logout/')
@login_required
def logout():
    #注销 退出
    #logout_user()
    #login_user
    #login_required
    # @login_manager.user_loader
    # @login_manager.user_loader
    #@login_manager.user_loader
    #def get_user(uid):
    #   return User.query.get(int(uid))
    #
    #
    # if current_user.is_authenticated:
    current_app.logger.warning(current_user.nickname + '退出了')
    logout_user()
    return redirect(url_for('web.index'))