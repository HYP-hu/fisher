"""
    create by misslove
"""
from flask import current_app, render_template
from flask_mail import Message
from threading import Thread
from app import mail

__author__ = 'misslove'
def send_async_email(app,msg):
    print('app',app,id(app))
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            app.logger.info('邮件发送出现错误!')

def send_mail(to,subject,template,**kwargs):
    # msg = Message('测试邮件',sender='841191837@qq.com',body='Test',
    #               recipients=['841191837@qq.com'])
    # mail.send(msg)
    msg = Message('[鱼书]'+' '+subject,sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])

    msg.html = render_template(template,**kwargs)
    app = current_app._get_current_object()
    print('current_app', current_app,id(current_app))
    print('app_obj',app,id(app))
    t=Thread(target=send_async_email,args=[app,msg])
    t.start()

