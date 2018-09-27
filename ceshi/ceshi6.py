"""
    create by misslove
"""
from functools import wraps

__author__ = 'misslove'


def decorate(fun):


    # @wraps(fun)
    def f(*args, **kwargs):

        fun(*args, **kwargs)
        print(fun.__name__)
        print(fun.__doc__)
        return fun
    return f


@decorate
def A():
    """
        这是文章A
    """
    pass
    # def __init__(self):
    #     self.a = 1
    #     self.b = 2
    # @staticmethod
    # def work():
    #     pass

a = A()
print(A)

print(A.__name__)
print(a.__name__)