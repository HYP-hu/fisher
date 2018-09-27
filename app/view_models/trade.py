"""
    create by misslove
"""
from app.view_models.book import BookViewModel

__author__ = 'misslove'

class TradeInfor():
    def __init__(self,goods):
        self.total = 0
        self.trades = []
        self.__parse(goods)


    def __parse(self,goods):
        self.total = len(goods)
        self.trades= [self.__map_to_trade(single) for single in goods]

    def __map_to_trade(self,single):
        if single.create_time:
            time = single.create_datetime.strftime('%Y-%m-%d')
        else:
            time = '未知'
        single_trade = {
            'user_name':single.user.nickname,
            'time':time,
            'id':single.id,
        }

        return single_trade

# class MyGifts():
    #赠送清单
    #用户的id所对应的所有isbn号 isbn列表
    #每个isbn所对应wish表的isbn的数量
    #所需要的数据
    #{
    #     'id':gift.id,
    #     'count':count(wish.id),


    #     'isbn':BookViewModel
    # }
    #gifts_list = Gift.query.filter_by(launched=False,uid=uid)
    # isbn_list = [gift.isbn for gift in gifts_list]
    #   count(wish.id,) wish.id        wish.isbn in isbn_list group_by(wish.isbn)
    #
    # for wish in wishes_list:
    #     wish.isbn == isbn
    # {
    #     isbn:isbn
    #     count:wish['count']
    #      id  :wish['id']
    # }

    #for gift in gifts_list:
    #
        #if
    # def __init__(self,gifts_list,wish_counts):
    #     self.trade = []
    #     self.gifts_list = gifts_list
    #     self.wish_counts = wish_counts
    #     self.trade = self.index
    #
    # def __parse(self,gift):
    #     yushu_book = YuShuBook()
    #     yushu_book.search_by_isbn(gift.isbn)
    #
    # def __collection(self,gifts):
    #     self.index = []
    #     for gift in self.gifts_list:
    #         result = self.__counts(gift)
    #         self.index.append(result)
    #
    # def __counts(self,gift):
    #
    #     for wish_count in self.wish_counts:
    #         if wish_count['isbn'] ==gift.isbn:
    #             result = {'count':wish_count['count'],
    #                       'book':BookViewModel(self.__parse(gift).first),
    #                       'id':gift.id
    #                       }
    #             return result

class MyTrades:
    def __init__(self, trades_of_mine, trade_count_list):
        self.trades = []
        self.__trades_of_mine = trades_of_mine
        self.__trade_count_list = trade_count_list
        self.trades = self.__parse()

    def __parse(self):
        temp_trades = []
        for trade in self.__trades_of_mine:
            my_trade = self.__matching(trade)
            temp_trades.append(my_trade)
        return temp_trades

    def __matching(self, trade):
        count = 0
        for trade_count in self.__trade_count_list:
            if trade.isbn == trade_count['isbn']:
                count = trade_count['count']
        r = {
            'count': count,
            'book': BookViewModel(trade.book),
            'id': trade.id
        }
        return r





