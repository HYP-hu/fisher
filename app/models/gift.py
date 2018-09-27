"""
    create by misslove
"""
from flask import current_app
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, desc, func
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from app.spider.yushu_book import YuShuBook

__author__ = 'misslove'


class Gift(Base):

    id = Column(Integer,primary_key=True)
    user = relationship('User')
    uid = Column(Integer,ForeignKey('user.id'))
    isbn = Column(String(15),nullable=False)
    launched = Column(Boolean,default=False)

    def is_yourself_gift(self,uid):
        return True if self.uid == uid  else False

    @classmethod
    def get_user_gifts(cls,uid):
        gifts=Gift.query.filter_by(uid=uid, launched=False).order_by(
            cls.create_time).all()
        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        from app.models.wish import Wish
        Wish_counts=db.session.query(func.count(Gift.id), Wish.isbn).filter(
            Wish.launched==False,
            Wish.isbn.in_(isbn_list),
            Wish.status==True,
        ).group_by(Wish.isbn).all()

        count_list = [{'count':wish[0], 'isbn':wish[1]} for wish in Wish_counts]
        return count_list

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def recent(cls):

        #对象代表一个礼物
        #类代表礼物这个事物,它是抽象的,不是具体的"一个"
        #一个礼物取多个方法确实是不合适的 用类方法
        #链式调用  极大的灵活性
        # 显示最近上传的数据
        # 限制展示30本
        # 展示的书本不可以重复
        # 展示的书本按时间排列
        # select
        # distinct
        # isbn, status, launched, create_time
        # from gift where
        # launched = 1 and status = 1 and create_time in (select max(create_time)
        # from gift group
        # by
        # isbn)  order
        # by
        # create_time
        # desc
        # limit
        # 10;

        recent_gifts = Gift.query.filter(Gift.launched==False,
        Gift.create_time.in_(db.session.query(func.max(Gift.create_time)).filter_by().group_by(Gift.isbn))
        ).order_by(desc(Gift.create_time)).distinct().limit(current_app.config['RECENT_BOOK_COUNTS']).all()

        # recent_gifts = Gift.query.filter_by(
        #     launched=False).group_by(
        #     Gift.isbn).order_by(
        #     desc(Gift.create_time)).distinct().limit(
        #     current_app.config['RECENT_BOOK_COUNTS']).all()
        # group_by(
        #     Gift.isbn).order_by(
        #     desc(Gift.create_time)).distinct().limit(
        #     current_app.config['RECENT_BOOK_COUNTS'])
        return recent_gifts
