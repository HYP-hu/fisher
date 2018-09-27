# # # """
# # #     create by misslove
# # # """
# # # __author__ = 'misslove'
# # # #装饰器模式的单例模式
# # # def decorator(cls):
# # #     _instance = {}
# # #     def f(*args,**kwargs):
# # #         if cls not  in _instance:
# # #             _instance[cls] = cls(*args,**kwargs)
# # #         return _instance[cls]
# # #     return f
# # #
# # # @decorator
# # # # class A():
# # # #     pass
# # # # a1 = A()
# # # # a2 = A()
# # # # print(id(a1),id(a2))
# # # #
# # # # @decorator
# # # # class B:
# # # #     pass
# # # # b1 = B()
# # # # b2 = B()
# # # # print(id(b1),id(b2))
# # # #
# # # # @decorator
# # # # class C():
# # # #     pass
# # # # c1 = C()
# # # # c2 = C()
# # # # print(id(c1),id(c2))
# # # # print('类实现单例模式')
# # # #
# # # # class Mycalss():
# # # #     _isinstance = None
# # # #     def __new__(cls, *args, **kwargs):
# # # #         if not cls._isinstance:
# # # #             cls._isinstance = super(Mycalss,cls).__new__(cls,*args,**kwargs)
# # # #             print(cls._isinstance)
# # # #         return cls._isinstance
# # # # print(Mycalss)
# # # # print(id(Mycalss))
# # # # a1 = Mycalss()
# # # # a2 = Mycalss()
# # # # a3 = Mycalss()
# # # # print(id(a1),id(a2),id(a3))
# # # # for i in range(10,101):
# # # #     if i % 3 == 0 or i % 5 == 0:
# # # #         print(i)
# # # # 介绍下MVC开发模式
# # # # from flask import Flask, make_response
# # #
# # # # app = Flask(__name__)
# # # #
# # # # @app.route('/index')
# # # # def search():
# # # #     response = make_response('hello',302)
# # # #     headers={
# # # #         'location':'http://www.baidu.com'
# # # #     }
# # # #     response.headers = headers
# # # #     # return 'hello',302,{
# # # #     #     'location': 'http://www.baidu.com'
# # # #     # }
# # # #     return response
# # # # if __name__ == '__main__':
# # # #     app.run(host='0.0.0.0',port='8888',threaded=True)
# # # #
# # # # A = [1,2,[3,4,['434',5,6],7],8,9,10]
# # #
# # # # def f(A):
# # # #     for i in A:
# # # #         if isinstance(i,list):
# # # #             f(i)
# # # #         else:
# # # #             print(i)
# # # # f(A)
# # # # m models 模型 MVC models
# # # # t templates  MVC views
# # # # v views  MVC controller
# # # # 401 403 404
# # # # 500
# # # # mysql
# # # #尽量避免全局搜索
# # # #选择合适的引擎
# # # # in not in != or 模糊查询避免%开头
# # # #
# # # # class A():
# # # #     def __init__(self):
# # # #         pass
# # # #     @classmethod
# # # #     def get(cls):
# # # #         pass
# # # #     @staticmethod
# # # #     def add(a,b):
# # # #         return a+b
# # # # a = A()
# # # # print()
# # # # value = a.add(1,2)
# # # # print(value)
# # # # c = A.add(1,2)
# # # # print(c)
# # # # class A():
# # # #     def __len__(self):
# # # #         return 0
# # # #     def __bool__(self):
# # # #         return False
# # # # a = A()
# # # # print(len(a))
# # # # print(bool(a))
# # # # class Myclass():
# # # #     _isinstance = None
# # # #     def __new__(cls, *args, **kwargs):
# # # #         if not cls._isinstance:
# # # #             cls._isinstance = super(Myclass,cls).__new__(cls,*args,**kwargs)
# # # #             print(cls._isinstance)
# # # #             print(type(cls._isinstance))
# # # #         return cls._isinstance
# # # # print(Myclass)
# # # # print(id(Myclass))
# # # # a1 = Myclass()
# # # # print(a1)
# # # # a2 = Myclass()
# # # # a3 = Myclass()
# # # # print(a1 is a2 )
# # # # print(a2 is a3)
# # # #100以内的
# # #
# # # # a b
# # # # from functools import lru_cache
# # # #
# # # #
# # # # class Fabnacci():
# # # #     def __init__(self,n):
# # # #         a,b = 0,1
# # # #         self.n = n
# # # #         self.a = a
# # # #         self.b = b
# # # #     def __iter__(self):
# # # #         while self.b < self.n:
# # # #             yield self.b
# # # #             self.a,self.b = self.b,self.a+self.b
# # # # f = Fabnacci(100)
# # # # for i in f:
# # # #     print(i)
# # # #
# # # # def fibonacci(n):
# # # #     a,b = 0,1
# # # #     while b < n:
# # # #         print(b)
# # # #         a,b = b,a+b
# # # # fibonacci(100)
# # # # print('~~~~~~~~~~~~~~~~~~~~~')
# # #
# # # # @lru_cache()
# # # # def fibonacci(n):
# # # #     # 1,1,2,3,5
# # # #     if n < 2:
# # # #         print(1)
# # # #         return 1
# # # #     else:
# # # #         value = fibonacci(n-2)+fibonacci(n-1)
# # # #         print(value)
# # # #         return value
# # # #
# # # # f = fibonacci(100)
# # # import functools
# # # from contextlib import contextmanager
# # #
# # # d = {'1':1,'2':2,'3':{},'4':[1,2,3,4],frozenset({1,2,3}):'hello'}
# # # print('~~~~~')
# # # L = dict()
# # # print('~~~~~~~~~~')
# # # class Ishash():
# # #     def __init__(self,value):
# # #         self.value = value
# # #     def __enter__(self):
# # #
# # #         return self
# # #         # return hash(self.value)
# # #     def __exit__(self, exc_type, exc_val, exc_tb):
# # #         return True
# # # for key,value in d.items():
# # #     with Ishash(value):
# # #         hash(value)
# # #         L.setdefault(value, key)
# # # print(L)
# #
# # # with Ishash()
# # #
# # #     try:
# # #         L.setdefault(value, key)
# # #     except Exception as e:
# # #         L.setdefault(key, value)
# # #
# # # print(L)
# # #
# # # @contextmanager
# # # def auto_commit(L,key,value):
# # #     try:
# # #         yield
# # #         L.setdefault(value, key)
# # #     except Exception as e:
# # #         L.setdefault(key, value)
# # #
# # #
# # #     for key,value in d.items():
# # #         with auto_commit(L):
# # #             pass
# #
# # # @contextmanager
# # # def f():
# # #     a = '<<'
# # #     b = '>>'
# # #     yield a,b
# # #
# # #
# # #
# # #
# # # with f() as c:
# # #     print(c[0]+'花一样的世界'+c[1])
# #
# #     # <<花一样的世界>>
# # # print(''''' ''''')
# # # list1 = [{'mm':2},{'mm':1},{'mm':4},{'mm':3},{'mm':3}]
# # # #从大到小
# # # L = sorted(list1,key=lambda x:x['mm'],reverse=True)
# # # print(L)
# # # #第二题没看懂
# # # result = [ d for d in  list1 for key,value in d.items() if value=='x']
# # # print(result)
# #
# # def f(*args,**kwargs):
# #     print(args)
# #
# # f({1:2})
# # f({1,2,3,4,5,6,7,8})
# # L = map(lambda x,y,z,w:x*y*z*w ,range(10),[1,2,3,4,5],[1,2,3,4,5],[0,0,0,0,0])
# # print(list(L))
# # from collections import Iterable,Iterator,Callable,Hashable,Generator
# # import collections
# # kk = collections.UserDict(k=1,c = 2)
# # value = (1,2)
# # value1 = {1,2,3}
# # value2 = [1,2,3,4]
# # value3 = frozenset({1,2,3,4,5})
# # print('value',isinstance(value,Hashable))
# # print('value',isinstance(value1,Hashable))
# # print('value',isinstance(value2,Hashable))
# # print('value',isinstance(value3,Hashable))
# #
# # print(kk)
# # class A():
# #     def __init__(self):
# #         pass
# #     def __iter__(self):
# #         pass
# #         # return self
# #     def __next__(self):
# #         pass
# #     def __call__(self, *args, **kwargs):
# #         pass
# # a = A()
# # b = [1,2,3,4,5]
# # k = set('12345')
# # print('~~~~~~~~~~~~~~')
# # print(k)
# # print(isinstance(a,Callable))
# # print('++++++++++++++')
# # n1 = dict(zip({1,2,3,4,5},{3,4,5,6,7,8}))
# # n2 = dict(a = 1,b = 2,c = 3)
# #
# # print(n1,isinstance(n1,Iterable))
# # print(n2)
# # list
# # is_Iterable = isinstance(n1,Iterable)
# # is_Iterator = isinstance(a,Iterator)
# # It = (it for it  in {1,2,3,4,5,6})
# # print(is_Iterable)
# # print(is_Iterator)
# # print(isinstance(It,Generator))
# # print(isinstance(It,Iterable))
# # # [  for key,value in d.items() if ]
# # # print(L)
# #冒泡排序
#
#
# L = [1,11,3,65,4,89,15,2,200,45,68,81,19]
# for i in range(len(L)-1):
#     for j in range(i+1,len(L)):
#         if L[i] < L[j]:
#             L[i],L[j] = L[j],L[i]
# print(L)
# #插入排序
# # L = [1,11,3,65,4,89,15,2,200,45,68,81,19]
# #
# # for i in range(len(L)):
# #     max = i+1
# #     j = 0
# #     while j < max:
# #         if L[i] > L[max]:
# #             L[max] = L[i]
# #             L[i+1] = L[max]
# #             L[i] =
#
# # L = [1,1,2,4,4,5,5,6,7,8,9,9]
# # for i in L:
# #     if L.count(i) != 1:
# #         for j in range(L.count(i)-1):
# #             L.remove(i)
# # print(L)
# # def del_same(L):
# #     for i in L:
# #         if L.count(i) != 1:
# #             for j in range(L.count(i)-1):
# #                 L.remove(i)
# #     return len(L)
# # f = del_same([1,2,3,4,5,6,7,3,2,1,2])
# # print(f)
# from collections import  Hashable
# class MyHashMap(object):
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.d = {}
#     def put(self, key, value):
#         """
#         value will always be positive.
#         :type key: int
#         :type value: int
#         :rtype: void
#         """
#         if isinstance(key,Hashable):
#
#             self.d.pop(key,value)
#             self.d.setdefault(key,value)
#         else:
#             raise ValueError('key不符合规范')
#
#     def get(self, key):
#         """
#         Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
#         :type key: int
#         :rtype: int
#         """
#         return self.d.get(key,-1)
#
#     def remove(self, key):
#         """
#         Removes the mapping of the specified
#         value key if this map contains a mapping for the key
#         :type key: int
#         :rtype: void
#         """
#         if  key in self.d:
#
#             del self.d[key]
#         else:
#             raise ValueError('不存在该键')
#
# hash = MyHashMap()
# from collections import Iterable, Iterator


# def del_same(L):
#     lst = reversed(L)
#     for i in lst:
#         if L.count(i) != 1:
#             for j in range(L.count(i)-1):
#                 L.remove(i)
#         print(L)
#     return len(L)
# f = del_same([1,2,3,1,2,3,1])
# class A(object):
# 	_isinstance = None
# 	def __new__(cls,*args,**kwargs):
# 		if not cls._isinstance:
# 			cls._isinstance = super(A,cls).__new__(cls,*args,**kwargs)
# a = A()
# b = A()
# print(a is b)
#
# # 装饰器的单例模式
# def decorate(f):
#     _isinstance = {}
#     def func(*args,**kwargs):
#         if f not in _isinstance:
#             _isinstance[f] = f(*args,**kwargs)
#         return _isinstance[f]
#     return func
#
# @decorate
# def f(*args,**kwargs):
#     pass
# a = f()
# b = f()
# print(a is b)
#什么是装饰器
#装饰器是一个函数 用来装饰一个函数 其本质是 在不改变原有功能的情况下添加额外的功能
#用于 AOP的切面编程 性能测试 插入日志 权限 缓存 事务等
#什么是面向对象
#面向对象
# 面向对象OOP  面向对象 python中讲究一切皆对象，具体而言就是使我们的程序模块化 对象化
#对于具体的事物 把它特征的属性，以及这些属性所产生的行为封装在类中，面向对象的三大特征
#封装继承多态
#lambda函数 匿名函数 lambda表达式 返回值为：后面的部分
# 可以随时创建和销毁 #函数名过多重复的现象 #
#水平触发 只要满足条件就触发
#边缘触发 只要状态改变就触发
#python内存管理机制 引用计数 垃圾清除 分代回收 标记清除 内存池 内存池内存池机制
#read读取整个文件 #readline读取一行 使用生成器的方法 #readlines使用的迭代器的方法
# import os
# def f(Dir):
#     l = os.listdir(Dir)
#     for i in l:
#         print(Dir + '\\'+ i)
#     print(os.path.dirname(Dir))
#     # print(os.path.basename(Dir))
#
# f('D:\QQ')
# L = [lambda :x for x in range(5)]
# print(L)
# for i in L:
#     print(i)
#     print(i())

# def f():
#     L = []
#     for i in  range(5):
#         print('ii',i)
#         def lam():
#             print('iiiiiiiiiii',i)
#             return i
#         L.append(lam)
#         print('LLL',L)
#     return L
# f1 = f()
# print('~~~~~~~~~~~~')
# print(f1[0]())
# def fun(n):
#     if n <= 1:
#         raise '不是质数'
#     for i in range(2,n//2+1):
#         if n % i == 0 :
#             return False
#     return True
#
# L = []
# def f(n):
#     if fun(n):
#         L.append(n)
#     for  i in range(2,n//2+1):
#         if n % i == 0:
#             L.append(i)
#             f(n//i)
#             break
#
# f(2)
# print(L)
def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[right] = key
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)
array = [12,24,21,9,4,14,12,13,19,18]
quick_sort(array,0,9)
print(array)




