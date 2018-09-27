"""
    create by misslove
"""
from flask import request, make_response, json, flash, render_template, redirect, url_for
from flask_login import current_user

from app.forms.book import SearchForm
from app.libs.enums import PendingStatus
from app.libs.helper import is_isbn_or_key, check_isbn
from app.models.drift import Drift
from app.models.gift import Gift
from app.models.user import User
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookCollection, BookViewModel
from app.view_models.trade import TradeInfor

__author__ = 'misslove'
from . import web

@web.route('/book/search/')
def search():
    # result1 = request.args['q']
    # result2 = request.args['key']
    # print(request.args.to_dict())
    # print(result2)
    # print(result1)
    # response =  make_response('hello world',200)
    # header = {
    #     'content-type': 'text/plain',
    #     'location': 'http://www.baidu.com'
    # }
    # response.header = header
    # return response
    # return 'hello world',302,header
    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()
        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q,page)

        books.fill(yushu_book, q)
    else:
        flash('搜索的关键字不符合要求,请重新输入关键字')

    # return json.dumps( books, default=lambda o:o.__dict__ ) ,200 ,{'content-type':'application/json'}
    return render_template("search_result.html", books=books,form=form)

@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    # has_in_gifts = False
    # has_in_wishes = False
    # #判断是否是isbn格式的
    # if is_isbn_or_key(isbn)!='isbn':
    #     return False
    # #判断isbn是否存在
    # yushu_book = YuShuBook()
    # if  not yushu_book.search_by_isbn(isbn).first:
    #     return False
    # #列出图书详情
    # book = BookViewModel(yushu_book)
    # #几人想要 几人可赠 不允许及时赠送者又是请求者 并且只能请求赠送一次
    # gifts  = Gift.query.filter_by(isbn=isbn,launched=False).all()
    # wishes = Wish.query.filter_by(isbn=isbn,launched=False).all()
    # #显示赠送者 或请求者  什么时间 书的isbn号码 以时间格式进行排序
    # #先处理单本书籍
    # def __init__(self,gifts):
    #     self.total = 0
    #     self.trades=[]
    #     self.singles(gifts)
    # def singles(self,gifts):
    #     self.total = len(gifts)
    #     self.trades = [single(gift) for gift in gifts]
    # def single(gift):
    #     if not gift.create_time:
    #         time = '未知'
    #     else:
    #         time = gift.create_datetime().strftime('%Y-%m-%d %H:%M:%S')
    #     username = gift.user.nickname
    #     id = gift.user.id
    #     return {
    #         'time':time,
    #         'username':username,
    #         'id':id,
    #     }
    # #判断用户是否登录:
    # if current_user.is_authenticated:
    #     gift=Gift.query.filter_by(isbn=isbn,launched=False).first()
    #     if gift:
    #         has_in_gifts=True
    #     wish=Wish.query.filter_by(isbn=isbn,launched=False).first()
    #     if wish:
    #         has_in_wishes=True




    #isbn是否符合要求
    #单本书籍详情

    #赠书人赠书后 赠书身份 下面显示所有请求书的人的名字   把书籍加入赠书清单
    #默认情况下显示所有赠书人的信息
    #加入心愿清单后 请求身份 赠书人的信息 把书籍加入心愿清单
    #所有与本书相关的赠书人
    #所有与本书相关的请求书的人
    #
    if check_isbn(isbn):
        # drift_gift=None
        # drift_wish=None
        has_in_gifts = False
        has_in_wishes = False
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        book = BookViewModel(yushu_book.first)
        #判断用户是否已经登录     然后判断是赠书人(是否已经在赠书单中)还是索要书的人(是否已经在索要书单中)
        if current_user.is_authenticated:
            if Gift.query.filter_by(uid=current_user.id, isbn=isbn,
                                    launched=False).first():
                has_in_gifts = True

            if Wish.query.filter_by(uid=current_user.id, isbn=isbn,
                                    launched=False).first():
                has_in_wishes = True

            #查找isbn所对应的所有的礼物
            #查找isbn所对应的所有的心愿清单
            #查找所有 此书所有的赠书人
            #查找所有 此书所有的索要书的人
            #给所有 赠书人 或者 索要书的人 按照时间进行排序 依次显示 nickname time

            #已经发起请求鱼漂的书籍 不能再次发送鱼漂 所以赠送者的名字不能出现了
            #
            # drift_gift = Drift.query.filter_by(isbn = isbn,
            #                        requester_id = current_user.id,
            #                        _pending = PendingStatus.WAITING.value).first()
            # #已经发起赠送请求的鱼漂 不能再次发送鱼漂 所以请求者的名字不能出现了
            # drift_wish = Drift.query.filter_by(isbn=isbn,
            #                         gifter_id=current_user.id,
            #                         _pending=PendingStatus.WAITING.value).first()
        # if drift_gift:
        #     trade_gifts=Gift.query.filter(Gift.isbn==isbn,Gift.launched==False,
        #                                   drift_gift.isbn !=isbn).all()
        # else:
        trade_gifts= Gift.query.filter_by(isbn=isbn, launched=False).all()

        # if drift_wish:
        #     trade_wishes = Wish.query.filter(Wish.isbn == isbn, Wish.launched == False,
        #                                      drift_wish.isbn !=isbn).all()
        # else:
        trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()
        trade_wishes_model = TradeInfor(trade_wishes)
        trade_gifts_model = TradeInfor(trade_gifts)
        return render_template('book_detail.html',
                               wishes=trade_wishes_model,
                               gifts=trade_gifts_model,
                               book=book,
                               has_in_gifts=has_in_gifts,
                               has_in_wishes=has_in_wishes
                               )
    # trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    # trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()
    #
    # trade_wishes_model = TradeInfo(trade_wishes)
    # trade_gifts_model = TradeInfo(trade_gifts)
    #
    # return render_template('book_detail.html',
    #                        book=book, wishes=trade_wishes_model,
    #                        gifts=trade_gifts_model, has_in_wishes=has_in_wishes,
    #                        has_in_gifts=has_in_gifts)






