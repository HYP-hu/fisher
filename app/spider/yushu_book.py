"""
    create by misslove
"""
from flask import current_app
from app.libs.httper import HTTP

__author__ = 'misslove'
class YuShuBook():
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.books = []
        self.total = 0

    def search_by_isbn(self,isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.single_book(result)


    def single_book(self,data):
        if data:
            self.total = 1
            self.books.append(data)

    def search_by_keyword(self,keyword,page=1):
        url =self.keyword_url.format(keyword,current_app.config['PER_PAGE'],
                                     YuShuBook.calc(page))
        result = HTTP.get(url)
        self.collection_books(result)

    def collection_books(self,data):
        self.total = data['total']
        self.books = data['books']

    @staticmethod
    def calc(start):
        return (start - 1)*current_app.config['PER_PAGE']

    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None






