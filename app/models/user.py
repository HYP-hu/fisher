"""
    create by misslove
"""
from math import floor

from flask import current_app, flash
from flask_login import UserMixin
from sqlalchemy import String, Column, Integer, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app.libs.enums import PendingStatus
from app.libs.helper import check_isbn
from app.models.base import Base, db
from app import login_manager
from app.models.drift import Drift
from app.models.gift import Gift
from app.models.wish import Wish

__author__ = 'misslove'

class User(UserMixin,Base):
    id = Column(Integer,primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column('password', String(128), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0.5)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    #鱼豆必须大于1
    # 每索取两本书必须赠送一本书
    def can_send_drift(self):
        if self.beans < 1:
            return False
        success_gift_counts = Gift.query.filter_by(launched=True,uid=self.id).count()
        success_receive_count = Drift.query.filter_by(gifter_id=self.id,
                                pending=PendingStatus.SUCCESS).count()
        return True if floor(success_receive_count/2) \
                       <= success_gift_counts else False

    @property
    def summary(self):
        return {
            'nickname':self.nickname,
            'send_receive':str(self.send_counter)+'/'+str(self.receive_counter),
            'beans': self.beans,
            'emial':self.email,
        }


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,raw):
        self._password = generate_password_hash(raw)

    def check_password(self,raw):
        return check_password_hash(self._password,raw)

    def can_save_to_list(self,isbn):
        # 不允许一个用户同时赠送多本相同的图书
        # 一个用户不可能同时成为赠送这和索要者
        if check_isbn(isbn):
            gifting = Gift.query.filter_by(isbn=isbn, launched=False, uid=self.id).first()
            wishing = Wish.query.filter_by(isbn=isbn,launched=False,uid=self.id).first()
            if  gifting or wishing:
                return False
            return True
        return False

    def generate_token(self,expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'],expiration)
        temp = s.dumps({'id':self.id}).decode('utf-8')
        return temp

    @staticmethod
    def reset_password(token,new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except Exception as e:
            print('写日志',e)
            return False
        uid = data.get('id')
        user = User.query.get(int(uid))
        if not user:
            flash('该用户不存在!')
            return False
        with db.auto_commit():
            user.password=new_password
        return True





# @login_manager.user_loader
# def get_user(uid):
#     return User.query.filter_by(int(uid))

@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))





