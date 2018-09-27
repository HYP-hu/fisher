# from app.libs.email import send_email
# from app.models.gift import Gift
# from app.view_models.wish import MyWishes
# from flask import render_template, flash, redirect, url_for, request
# from flask_login import login_required, current_user
#
from flask import url_for, flash, render_template, request
from flask_login import login_required, current_user
from werkzeug.utils import redirect

from app import limiter
from app.libs.email import send_mail
from app.libs.enums import PendingStatus
from app.models.base import db
from app.models.drift import Drift
from app.models.gift import Gift
from app.models.wish import Wish
from app.view_models.trade import MyTrades
from . import web
# from app.spider.yushu_book import YuShuBook
# from app.service.wish import WishService
# from app import limiter

# from app.models import db
# from app.models.wish import Wish

__author__ = '七月'


# def limit_key_prefix():
#     isbn = request.args['isbn']
#     uid = current_user.id
#     return f"satisfy_wish/{isbn}/{uid}"

@web.route('/my/wish')
@login_required   #不登录的情况下拒绝被访问 和
def my_wish():
    #获取当前用户的id
    # uid = current_user.id
    # #Wish model关联 wid 用户 user  isbn uid
    # #通过id获取心愿清单
    # wishes = Wish.query.filter_by(uid=uid,launched=False).all()
    # #通过id获取礼物清单
    # #获取每本书的isbn列表
    # isbn_list = [wish.isbn for wish in wishes]
    # #通过每个isbn获取赠书人的数量
    #书籍详情
    #判断每个isbn是否存在 存在获取相应的图书信息
    # yushu_book = YuShuBook()
    # yushu_book.search_isbn()
    #
    # # for isbn in isbn_list:
    # #     gift_counts = Gift.query.filter_by(isbn=isbn).count()
    #       Gift.query(func.count(Gift.uid),Gift.isbn).filter(
    #           Gift.isbn.in_(isbn_list),
    #           launched=False,
    #       ).group_by(Gift.isbn).order_by(desc(Gift.create_time)).distinct().limit(30)
    # #     gift_dict_counts = {
    # #             'count':gift_counts,
    # #             'book': books
    # #                         }
    #
    #
    #
    # # gifts = Gift.query.filter_by(uid=uid,launched=False).all()
    # #

    uid = current_user.id
    my_wish_list=Wish.get_user_wishes(uid)
    my_isbn_list=[wish.isbn for wish in my_wish_list]
    gift_count_list=Wish.get_gift_counts(my_isbn_list)
    view_model = MyTrades(my_wish_list,gift_count_list)

    return render_template('my_wish.html', wishes=view_model.trades)


    # uid = current_user.id
    # wishes = Wish.query.filter_by(uid=uid, launched=False).all()
    # gifts_count = WishService.get_gifts_count(wishes)
    # view_model = MyWishes(wishes, gifts_count)
    # return render_template('my_wish.html', wishes=view_model.my_wishes)


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        wish = Wish()
        attrs_dict = {
            'isbn':isbn,
            'uid':current_user.id
        }
        with db.auto_commit():
            wish.set_attrs(attrs_dict)
            db.session.add(wish)
    else:
        flash('您已加入心愿清单,不能重复添加!')
    return redirect(url_for('web.book_detail',isbn=isbn))

# user.id isbn
# 第一次加载缓存日志
# 第二次读取缓存日志 时间超了 就触发下一个视图不允许重复点击
#
def limit_key_prefix():
    isbn = request.args['isbn']
    uid = current_user.id
    print('isbn',isbn,'uid',uid)
    return f'satisfy_wish/{isbn}/{uid}'

#向他人赠送此书
@web.route('/satisfy/wish/<int:wid>')
@limiter.limit(key_func=limit_key_prefix)
@login_required
def satisfy_wish(wid):
    wish = Wish.query.get_or_404(wid)
    gift = Gift.query.filter_by(uid=current_user.id, isbn=wish.isbn).first()
    if not gift:
        flash('你还没有上传此书，'
              '请点击“加入到赠送清单”添加此书。添加前，请确保自己可以赠送此书')
    else:
        send_mail(wish.user.email,
                  '有人想送你一本书', 'email/satisify_wish.html', wish=wish,
                  gift=gift)
        flash('已向他/她发送了一封邮件，如果他/她愿意接受你的赠送，你将收到一个鱼漂')
    return redirect(url_for('web.book_detail', isbn=wish.isbn))
    # if  gift:
    #     #Message( 开头 发送人 收件人)
    #     #send_mail函数(to,object,template,**kwargs)
    #     send_mail('841191837@qq.com','向你赠了一本书','email/satisify_wish.html',wish=wish,gift=gift)
    #     flash('已向他/她发送了一封邮件,如果他/她接受了你的赠送你将收到一个鱼漂')
    # else:
    #     flash('您还未有此书，请点击“加入到赠送清单”添加此书。添加前，请确保自己可以赠送此书')
    # return redirect(url_for('web.book_detail',isbn=wish.isbn))


@limiter.limited
def satisfy_with_limited():
    isbn = request.args['isbn']
    flash('你已向他/她发送赠送邀请,请不要频繁发送')
    return redirect(url_for('web.book_detail',isbn=isbn))


    # """
    #     向想要这本书的人发送一封邮件
    #     注意，这个接口需要做一定的频率限制
    #     这接口比较适合写成一个ajax接口
    # """
    # wish = Wish.query.get_or_404(wid)
    # gift = Gift.query.filter_by(uid=current_user.id, isbn=wish.isbn).first()
    # if not gift:
    #     flash('你还没有上传此书，请点击“加入到赠送清单”添加此书。添加前，请确保自己可以赠送此书')
    # else:
    #     send_email(wish.user.email, '有人想送你一本书', 'email/satisify_wish', wish=wish,
    #                gift=gift)
    #     flash('已向他/她发送了一封邮件，如果他/她愿意接受你的赠送，你将收到一个鱼漂')
    # return redirect(url_for('web.book_detail', isbn=wish.isbn))


# @web.route('/wish/book/<isbn>/redraw')
# # @login_required
# def redraw_from_wish(isbn):
#     pass

@web.route('/wish/book/<isbn>/redraw')
@login_required
def redraw_from_wish(isbn):
    wish = Wish.query.filter_by(isbn=isbn, launched=False).first_or_404()
    drift = Drift.query.filter_by(requester_id = wish.uid,
                                  _pending=PendingStatus.WAITING.value).first()

    if drift:
        flash('不能撤销，此书正在被赠送中....')
        return redirect(url_for('web.my_wish'))
    with db.auto_commit():
        wish.delete()
    return redirect(url_for('web.my_wish'))

