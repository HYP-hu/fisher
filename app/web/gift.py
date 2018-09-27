from flask import current_app, flash, redirect, url_for, render_template
from flask_login import login_required, current_user

from app.libs.enums import PendingStatus
from app.models.base import db
from app.models.drift import Drift
from app.models.gift import Gift
from app.view_models.trade import MyTrades
from . import web


__author__ = '七月'


@web.route('/my/gifts')
@login_required
def my_gifts():
    #赠送清单
    #显示所有赠送的书籍
    #显示多少人想要
    #按时间顺序排列
    # 赠送清单
    # 赠送的数量
    # 每本书有几个人想要
    # 撤销
    uid = current_user.id
    get_gifts_mine = Gift.get_user_gifts(uid)
    isbn_list = [gift.isbn for gift in get_gifts_mine]
    wish_count_list = Gift.get_wish_counts(isbn_list)
    view_model = MyTrades(get_gifts_mine,wish_count_list)
    return render_template('my_gifts.html',gifts=view_model.trades)


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    #添加赠送清单 赠书
    #1、 查询该书的详细信息
    #2、 用户有无此书
    #3、 赠送扣除鱼豆
    #4、 用户此书数量减一
    #5、 gift此书数量加一
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            gift = Gift()
            #如果赠送一本书就给 0.5个豆 那么我是不是可以多赠送基本但就是不给他 业务逻辑就错了
            #注册成功就给0.5个豆 每成功赠送一本书给0.8个豆
            # current_user.beans += current_app.config["BEANS_UPLOAD_ONE_BOOK"]
            data = {
                'isbn':isbn,
                'uid':current_user.id,
            }
            gift.set_attrs(data)
            db.session.add(gift)
    else:
        flash('这本书已经加入了您的赠送清单或已存您的心愿清单,请不要重复添加')
    return redirect(url_for('web.book_detail',isbn=isbn))

@web.route('/gifts/<gid>/redraw')
# @login_required
def redraw_from_gifts(gid):
    gift = Gift.query.filter_by(id=gid, launched=False).first_or_404()
    drift = Drift.query.filter_by(gifter_id=gift.uid,
                                  _pending=PendingStatus.WAITING.value).first()
    if drift:
        flash('不能撤销，此书正在被赠送中....')
        return redirect(url_for('web.my_wish'))
    with db.auto_commit():
        gift.delete()
    return redirect(url_for('web.my_gifts'))

