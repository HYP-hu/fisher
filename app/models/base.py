"""
    create by misslove
"""
from datetime import datetime

__author__ = 'misslove'

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, Integer, Boolean, DateTime
from contextlib import contextmanager


# 继承BaseQuery让所有status默认值为1
class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    create_time = Column('create_time', Integer)
    status = Column(Boolean, default=1)
    # create_time = Column('create_time', DateTime, default=datetime.now().timestamp())
    __abstract__ = True

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def set_attrs(self,attrs_dict):
        for key,value in attrs_dict.items():
            if hasattr(self,key) and key != id:
                setattr(self,key,value)

    def delete(self):
        self.status = 0


    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None






