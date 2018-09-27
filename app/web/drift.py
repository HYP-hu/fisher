from flask import flash, redirect, url_for, render_template, request
from flask_login import current_user, login_required
from sqlalchemy import or_, desc
from app.forms.drift import DriftForm
from app.libs.email import send_mail
from app.libs.enums import PendingStatus
from app.models.base import db
from app.models.drift import Drift
from app.models.gift import Gift
from app.models.user import User
from app.models.wish import Wish
from app.view_models.book import BookViewModel
from app.view_models.drift import DriftCollection
from . import web

__author__ = '七月'


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
@login_required
def send_drift(gid):
    #
    #自己不能够向自己请求书籍
    #礼物是否在wish清单中
    #
    #鱼豆必须大于1才能请求书籍
    #每索取两本书必须赠送一本书

    #发送鱼漂 向他人请求此书
    #查询该礼物是否在赠送清单内
    #current_gift=Gift.query.get_or_404(gid)
    #自己不能向自己请求书籍
    #此书一定要在心愿清单中
    #每索取两本书必须赠送一本书
    # self.beans < 1
    #   return False
    #success_gift_counts=Gift.query.filter_by(id=current_user.id,launched=True).count()
    #success_wish_counts=Wish.query.filter_by(id=current_user.id,launched=True).count()
    #success_receive_counts = Drift.query.filter_by(
    # requester_id=current_user.id,status=PendingStatus(SUCCESS))
    #
    #import math
    #True if math.floor(success_wish_counts/2)<success_gift_counts else False
    # return render_template('not_enough_beans.html',beans=current_user.beans')
    #渲染模板
    #这本书的详细信息  在model或者在view_model操作
    #我们在model里面操作
    #名字鱼豆,接收和送出的书籍
    #
    #class User():
    #@property
    #赠送者的信息
    #gifter = current_gift.user.summary
    #def summary():
    #   return {
    #   nickname:self.nickname,
    #   beans:self.beans,
    #   receive_counter:self.receive_counter,
    #   send_counter:self.send_counter,
    # }
    #form = DriftForm(request.form)
    #if request.method=='POST' and form.validator():
    #   save_drift(form,current_gift)
    # 发送邮件
    #   send_mail(to,subject,template,**kwargs)
    #   send_mail(current_gifter.user.email,'请求一本书','drift.html',gift=current_gift,wisher=current_user)
    #   msg = Message('鱼书'+ ' ' + object,sender=current_app.config['MAIL_USERNAME'],
    # recipents=[to])
    #   msg.html = render_template()
    #   mail.send(msg)
    #   return redirect(url_for('web.pending'))
    #
    #
    #
    #   #保存信息到数据库(自定义函数)
    # def save_drift(drift_form,current_gift):
    #   with db.auto_commit():
    #       drift=Drift()
    #       邮寄信息
    #       drift.set_attrs(drift_form.data)
    #       drift_form.populate_obj(drift)
    #       drift_form.populate_obj(drift)
    #       书籍信息
    #       book = BookViewModel(current_gift.book)
    #       drift.isbn = book.isbn
    #       drift.book_title = book.title
    #       drift.book_author = book.author
    #       drift.book_img = book.image
    #       请求者的信息
    #       drift.requester_id = current_user.id
    #       drift.request_nickname = current_user.nickname
    #       赠送者信息
    #       drift.gifter_id = current_gift.uid
    #       drift.gift_id = current_gift.id
    #       drift.gifter_nickname = current_gift.user.nickname
    #
    #       try:
    #           if current_user.beans < 1 :
    #               raise ValueError
    #       except except Exception as e:
    #               print('写日志')
    #       db.session.add(drift)
    #
    #return render_template('drift.html',gifter=gifter,beans=current_user.beans,form=form)
    current_gift = Gift.query.filter_by(id=gid,launched=False).first_or_404()
    current_wish = Wish.query.filter_by(launched=False,isbn=current_gift.isbn,
                                        uid = current_user.id).first()
    #不允许两个赠送者都给你发了邮件 你打开链接同时 提交 出现两个pending的情况 所以 你
    #填写了第一个drift表单 第二个drift表单不允许再被提交！
    drift = Drift.query.filter_by(_pending=PendingStatus.WAITING.value,
                                  isbn=current_gift.isbn,
                                  requester_id=current_user.id).first()
    #你给两个请求者都发了邮件 一个请求者 填写后 另一个不允许再被填写
    drift1 = Drift.query.filter_by(_pending=PendingStatus.WAITING.value,
                                   isbn=current_gift.isbn,gifter_id = current_gift.uid)
    if drift1:
        flash('你来晚了哦,此书已经被他人赠送了!')
        return redirect(url_for('web.book_detail',isbn=current_gift.isbn))
    if drift:
        flash('你已经填写过表单了,不允许再被填写了!')
        return redirect(url_for('web.book_detail', isbn=current_gift.isbn))
    if not current_wish:
        flash('您还未把此书加入心愿清单,不能所要书籍哦')
        return redirect(url_for('web.book_detail', isbn=current_gift.isbn))
    if current_gift.is_yourself_gift(current_user.id):
        flash('这本书是你自己的^_^,不能向自己索要书籍噢')
        return redirect(url_for('web.book_detail',isbn=current_gift.isbn))
    if not current_user.can_send_drift():
        return render_template('not_enough_beans.html',beans=current_user.beans)
    #所有条件均满足 渲染模板
    #书籍赠送者信息
    gifter = current_gift.user.summary
    form = DriftForm(request.form)
    if request.method=='POST' and form.validate():
        save_drift(form,current_gift)
        send_mail(current_gift.user.email,'有人想要一本书','email/get_gift.html',
                  wisher=current_user,gift=current_gift)
        return redirect(url_for('web.pending'))

    return render_template('drift.html',gifter=gifter,user_beans=current_user.beans,
                         form=form)


@web.route('/pending')
@login_required
def pending():
    #交易记录
    #查询drift表
    drift = Drift.query.filter(or_(Drift.requester_id==current_user.id,
                               Drift.gifter_id==current_user.id)).order_by(
                               desc(Drift.create_time)).all()

    views = DriftCollection(drift,current_user.id).data

    return render_template('pending.html',drifts = views)

    #交易查询

    # 对drifter原始数据处理
    #单个处理
    #多个处理
@web.route('/drift/<int:did>/mailed')
@login_required
def mailed_drift(did):
    #赠送者才能   确认成功 或者 失败
    #功能 最好发送发送邮件邮寄(告知已经邮寄)
    with db.auto_commit():
        drift = Drift.query.filter_by(gifter_id=current_user.id,
                                      id = did
                                      ).first_or_404()
        #状态改为1
        drift.pending = PendingStatus.SUCCESS
        # gift1 = Gift.query.get_or_404(int(drift.gift_id))
        # print('gift1gift1',gift1)
        current_user.beans += 1
        gift = Gift.query.filter_by(id=drift.gift_id,launched=False
        ).first_or_404()
        # gift = Gift.query.get_or_404(int(drift.gift_id))
        current_user.beans += 1
        gift.launched = True
        current_user.send_counter +=1

        # 一个心愿被多个人赠送 此时心愿表单的处理
        # 心愿表单的uid isbn launched
        # wish = Wish.query.filter_by(isbn=gift.isbn,launched=False,
        #                      uid = drift.requester_id
        #                      ).update({Wish.launched: True})
        wish = Wish.query.filter_by(isbn=gift.isbn,launched=False,
                             uid = drift.requester_id
                             ).first_or_404()
        wish.launched = True
        wish.user.receive_counter += 1
        wish.user.beans -= 1
        return redirect(url_for('web.pending'))





















def save_drift(drift_form,current_gift):
    with db.auto_commit():
        drift =Drift()
        # 邮寄信息
        # drift_form.populate_obj(drift)
        drift.set_attrs(drift_form.data)
        # 书籍信息
        book = BookViewModel(current_gift.book)
        drift.isbn = book.isbn
        drift.book_title = book.title
        drift.book_author = book.author
        drift.book_img = book.image
        # 请求者信息
        drift.requester_id = current_user.id
        drift.requester_nickname = current_user.nickname
        # 赠送者信息
        drift.gifter_id = current_gift.user.id
        drift.gift_id = current_gift.id
        drift.gifter_nickname = current_gift.user.nickname
        try:
            current_user.beans -= 1
            if current_user.beans < 0:
                raise ValueError
        except Exception as e:
            print('写日志')
            raise e
        db.session.add(drift)



@web.route('/drift/<int:did>/reject')
@login_required
def reject_drift(did):
    pass
    # """
    #     拒绝请求，只有书籍赠送者才能拒绝请求
    #     注意需要验证超权
    # """
    with db.auto_commit():
        #查询drift表中是否有此书籍信息
        drift = Drift.query.filter_by(id=did,gifter_id=current_user.id,
                                   _pending=PendingStatus.WAITING.value).first_or_404()
        drift.pending = PendingStatus.REJECT
        # 请求者的鱼豆要加1
        user = User.query.filter_by(id=drift.requester_id).first_or_404()
        user.beans += 1
        return redirect(url_for('web.pending'))

@web.route('/drift/<int:did>/redraw')
@login_required
def redraw_drift(did):
    # """
    #     撤销请求，只有书籍请求者才可以撤销请求
    #     注意需要验证超权
    # """
    with db.auto_commit():
        drift = Drift.query.filter_by(id=did,
                requester_id=current_user.id,_pending=PendingStatus.WAITING.value).first_or_404()
        drift.pending = PendingStatus.REDRAW
        user = User.query.filter_by(id=current_user.id).first_or_404()
        user.beans += 1
        return redirect(url_for('web.pending'))














    # with db.auto_commit():
    #     # requester_id = current_user.id 这个条件可以防止超权
    #     # 如果不加入这个条件，那么drift_id可能被修改
    #     drift = Drift.query.filter_by(
    #         requester_id=current_user.id, id=did).first_or_404()
    #     drift.pending = PendingStatus.redraw
    #     current_user.beans += current_app.config['BEANS_EVERY_DRIFT']
    #     # gift = Gift.query.filter_by(id=drift.gift_id).first_or_404()
    #     # gift.launched = False
    # return redirect(url_for('web.pending'))



