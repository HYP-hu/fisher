"""
    create by misslove
"""
from enum import Enum,IntEnum,unique

__author__ = 'misslove'
class A(Enum):
    a = 1
    b = 2
    c = 3
print(A)
print(A.__class__)
print(dir(A))
print(A.__members__)
print(A['a'])
print(A.a.name)
print(type(A.a.name))
print('---------')
test1 = A.a
print(A.a)
print(A(A.a))
print(A(1) is A(1))
print('++++++')
test2 = A.a
print(test1 is test2)
for i in A:
    print(i)
class B():
    a = 1
    b = 2

print(B() is B())




# print(A(1))
# print(type(A(2)))
#
# print(A.a)
# print(type(A.a))
# print(A.a.value)
# print(A.b.value)
# print(A.c.value)