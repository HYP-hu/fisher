"""
    create by misslove
"""
from flask import Blueprint, render_template, current_app

__author__ = 'misslove'

web = Blueprint('web',__name__)


@web.app_errorhandler(404)
def not_found(e):
    current_app.logger.info('发生了错误哦！！！！')
    #AOP 思想   这里也可以用来处理日志
    return render_template('404.html'),404

@web.app_errorhandler(500)
def server_error(e):
    #AOP 思想   这里也可以用来处理日志
    return render_template('500.html'),500
from app.web import book
from app.web import author
from app.web import drift
from app.web import main
from app.web import gift
from app.web import wish



