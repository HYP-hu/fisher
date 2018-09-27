"""
    create by misslove
"""
from app.libs.enums import PendingStatus

__author__ = 'misslove'


class DriftCollection:
    # 显示所有的交易记录
    def __init__(self, drifts, current_user_id):
        self.data = []

        self.__parse(drifts, current_user_id)

    def __parse(self, drifts, current_user_id):
        for drift in drifts:
            temp = DriftViewModel(drift, current_user_id)
            self.data.append(temp.data)


class DriftViewModel:
    #显示单本的交易记录
    def __init__(self,drift,current_user_id):
        self.data = {}
        self.data = self.__parse(drift,current_user_id)
    #判断是请求者还是赠送者
    @staticmethod
    def requester_or_gifter(drift, current_user_id):
        if drift.requester_id == current_user_id:
            you_are = 'requester'
        else:
            you_are = 'gifter'

        return you_are

    def __parse(self,drift,current_user_id):

        you_are = self.requester_or_gifter(drift,current_user_id)
        pending_status = PendingStatus.pending_str(drift.pending,you_are)
        #pending_status 状态,请求者或赠送者显示此时的状态
        r = {
            'you_are': you_are,
            'drift_id': drift.id,
            'book_title': drift.book_title,
            'book_author': drift.book_author,
            'book_img': drift.book_img,
            'date': drift.create_datetime.strftime('%Y-%m-%d'),
            'operator': drift.requester_nickname if you_are != 'requester'
            else drift.gifter_nickname,
            'message': drift.message,
            'address': drift.address,
            'status_str': pending_status,
            'recipient_name': drift.recipient_name,
            'mobile': drift.mobile,
            'status': drift.pending
        }
        return r





