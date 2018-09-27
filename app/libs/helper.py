"""
    create by misslove
"""
from app.spider.yushu_book import YuShuBook

__author__ = 'misslove'

def is_isbn_or_key(word):
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-','')
    if '-' in word and len(short_word)==10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key

def check_isbn(isbn):
    if is_isbn_or_key(isbn) != 'isbn':
        return False
    # 即不在赠送清单,也不在心愿清单才能添加
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    if not yushu_book.first:
        return False
    return True

