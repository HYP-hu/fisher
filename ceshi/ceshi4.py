"""
    create by misslove
"""
import inspect
from inspect import isfunction

__author__ = 'misslove'

def f1():
    pass

def f2():
    pass

def f3():
    pass

def f4():
    pass

def f5():
    pass

class A:
    def __call__(self, *args, **kwargs):
        pass

class B:
    pass
print(dir(B))
print(callable(B))
print(globals())
print('~~~~~~~~~~~~~~~~~~~~~~')
# gen =  [{key:value}  for key,value in globals().items() if value.startswith() and callable(value()) ]
# for i in gen:
#     print(i)
print(__name__)
import ceshi.ceshi1
print()
print(__name__)
for name,func in inspect.getmembers(ceshi.ceshi1,inspect.isfunction):
    print(name,':',func)