"""
    create by misslove
"""

__author__ = 'misslove'
# print('ddddddddddddddd')
# d = 4
# from ceshi.ceshi2 import c
# print('我是测试3的',c)
from collections import  Hashable
class MyHashMap(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
    def put(self, key, value):
        """
        value will always be positive.
        :type key: int
        :type value: int
        :rtype: void
        """
        if isinstance(key,Hashable):

            self.d.pop(key)
            self.d.setdefault(key,value)
        else:
            raise ValueError('key不符合规范')

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        return self.d.get(key,-1)

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        if  key in self.d:
            del self.d[key]
        raise ValueError('不存在该键')
L = MyHashMap()
