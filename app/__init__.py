"""
    create by misslove
"""
import logging
from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail

from app.libs.limiter import Limiter

mail = Mail()
from app.models.base import db
login_manager = LoginManager()
__author__ = 'misslove'
limiter = Limiter()
def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    register_blueprint(app)
    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = u'请先登录或注册'
    with app.app_context():
        db.create_all()
    db.create_all(app=app)
    logging.basicConfig(filename=r"/home/huyp/developer/practice/fisher/log/fisher.log",
                        format='%(asctime)s - %(name)s '
                               '- %(levelname)s - %(message)s')
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)


