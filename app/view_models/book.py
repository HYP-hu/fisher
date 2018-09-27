"""
    create by misslove
"""
__author__ = 'misslove'

class BookViewModel():
    def __init__(self,book):
        self.author = '、'.join(book['author'])
        self.title = book['title']
        self.price = book['price']
        self.image = book['image']
        self.publisher = book['publisher'] or ''
        self.price = book['price']
        self.summary = book['summary'] or ''
        self.pages = book['pages']
        self.isbn = book['isbn']
        self.binding = book['binding']
        self.pubdate = book['pubdate']

    @property
    def intro(self):
        intros = filter(lambda x:x,[self.author,self.publisher,self.price])
        return ' / '.join(intros)

class BookCollection():
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self,yushu_book,keyword):
        self.keyword = keyword
        self.total = yushu_book.total
        self.books = [
            BookViewModel(book) for book in yushu_book.books
        ]

