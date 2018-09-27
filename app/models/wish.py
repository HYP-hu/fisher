"""
    create by misslove
"""

from sqlalchemy import Integer, Column, Boolean, ForeignKey, String, func, desc
from sqlalchemy.orm import relationship
from app.models.base import Base, db

from app.spider.yushu_book import YuShuBook

__author__ = 'misslove'


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @classmethod
    def get_user_wishes(cls, uid):
        wishes = Wish.query.filter_by(uid=uid, launched=False).order_by(
            cls.create_time).all()
        return wishes

    @classmethod
    def get_gift_counts(cls, isbn_list):
        from app.models.gift import Gift
        count_list = db.session.query(func.count(Gift.id),Wish.isbn).filter(
            Gift.launched == False,
            Gift.isbn.in_(isbn_list),
            Gift.status == 1,
            ).group_by(Wish.isbn).all()

        count_list = [{'count': wish[0], 'isbn':wish[1]} for wish in count_list]
        return count_list

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first




