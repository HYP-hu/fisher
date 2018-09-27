"""
    create by misslove
"""
# import random
#
# __author__ = 'misslove'
# import unittest
# class Dict(dict):
#     def __init__(self,**kwargs):
#         super(Dict,self).__init__(**kwargs)
#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
#     def __setattr__(self, key, value):
#         self[key] = value

# d = Dict(a=1,b=2)
# print(d['a'])
# print(d.a)

# class TestDict(unittest.TestCase):
#
#     def test_init(self):
#         d = Dict(a=1,b='test')
#         self.assertEqual(d.a,1)
#         self.assertEqual(d.b,'test')
#         self.assertTrue(isinstance(d,dict))
#
#     def test_key(self):
#         d = Dict()
#         d['key'] = 'value'
#         self.assertEqual(d.key,'value')
#
#     def test_attr(self):
#         d = Dict()
#         d.key = 'value'
#         self.assertTrue('key' in d)
#         self.assertEqual(d['key'], 'value')
#
#     def test_keyerror(self):
#         d = Dict()
#         with self.assertRaises(KeyError):
#             value = d['empty']
#             print(d.__dict__)
#
#     def test_attrerror(self):
#         d = Dict()
#         with self.assertRaises(AttributeError):
#             value = d.empty
#
# if __name__ == '__main__':
#     unittest.main()

# def get_formmed_name(first, last):
#     """该函数根据姓和名生成一个完整的姓名"""
#
#     full_name = first + ' ' + last
#     return full_name.title()
#
# print(get_formmed_name('hello','world'))
# partition([6,1,2,7,9,3,4,5,10,8],)
# 6  1  2  7  9  3  4  5 10  8
# def quick_sort(array, l, r):
#     if l < r:
#         q = partition(array, l, r)
#         quick_sort(array, l, q - 1)  # quick_sort([2,3,1,4,5,9,6,7],0,2)  quick_sort([1,3,2,4,5,9,6,7])
#         quick_sort(array, q + 1, r)  #
#
#
# def partition(array, l, r):
#     x = array[r]
#     i = l - 1
#     for j in range(l, r):
#         if array[j] <= x:
#             i += 1
#             array[i], array[j] = array[j], array[i] #把小于x值的数 转到最左边
#     array[i + 1], array[r] = array[r], array[i + 1] #把游标值移到中间
#     return i + 1                     #游标值的索引
# L1 = [3,2,5,7,1,9,6,4]   # l=0 r=7
# quick_sort(L1,0,7)
# print(L1)

# [3,2,5,7,1,9,6,4]
# [3,2,1,7,5,9,6,4]  #循环结束 i=2
# [3,2,1,4,5,9,6,7]  #return i+1=>i=3
# quick_sort  q=3
# quick_sort([3,2,1,4,5,9,6,7],0,2)
# quick_sort([1,2,3,4,5,9,6,7])

# def quick_sort(array, left, right):
#     if left >= right:
#         return
#     low = left
#     high = right
#     key = array[low]
#     while left < right: #[3,2,5,7,1,9,6,4]   #[6,2,5,7,1,9,3,4]
#         while left < right and array[right] > key:
#             right -= 1              # right-1
#         array[left] = array[right] #[6,2,5,7,1,9,3,4]
#         while left < right and array[left] <= key:
#             left += 1     #[6,2,5,7,1,9,3,4]   left=1
#         array[right] = array[left]    #[3,2,5,7,9,6,4]
#                                       #[2,3,5,7,9,6,4]
#     array[right] = key    #
#     quick_sort(array, low, left - 1)
#     quick_sort(array, left + 1, high)
#
#
# L1 = [3,2,5,7,1,9,6,4]   # l=0 r=7
# quick_sort(L1, 0, 7)
# print(L1)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # nums = [2]
# nums = range(2,20)
# for i in nums:
#     nums = filter(lambda  x:x==i or x % i,nums)
#
# print(nums)
# print(type(nums))

# nums = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]


# import time
# def decorator(f):
#     def fun(*args,**kwargs):
#         start = time.perf_counter()
#         f(*args,**kwargs)
#         print(time.perf_counter()-start)
#     return fun
#
# @decorator
# def f1(lIn):
#     l1 = sorted(lIn)
#     l2 = [i for i in l1 if i<0.5]
#     l3 = [i*i for i in l2]
#     return
# @decorator
# def f2(lIn):
#     l1 = [i for i in lIn if i<0.5]
#     l2 = sorted(l1)
#     l3 = [i*i for i in l2]
#     return
# @decorator
# def f3(lIn):
#     l1 = [i*i for i in lIn]
#     l2 = sorted(l1)
#     l3 = [i for i in l1 if i < (0.5 * 0.5)]
#     return
#
# f1([random.random() for i in range(100000)])
# f2([random.random() for i in range(100000)])
# f3([random.random() for i in range(100000)])

# def print_directory_contents(sPath):
#     import os
#     for sChild in os.listdir(sPath):
#         sChildPath = os.path.join(sPath,sChild)
#         if os.path.isdir(sChildPath):
#             print_directory_contents(sChildPath)
#         else:
#             print(sChildPath)
#
# print_directory_contents(r'D:\QQ')
# b1 = [1,2,3]
# b2 = [2,3,4]
# #交集和差集
# for
D = dict(a=1,b=2,c=3,d=4)
for i in D.items():
    print(i)

D = dict(a=1,b=2,c=3,d=4)
for k,v in D.iteritems():
    print(i)








