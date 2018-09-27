"""
    create by misslove
"""
from flask import Flask as _Flask, json, jsonify
from flask.json import JSONEncoder as _JSONEncoder
__author__ = 'misslove'
class A:
    a = 1
    b = 2
    c = 3
    def keys(self):
        print('keys')
        return ['a','b','c']
    def __getitem__(self, item):
        print('getitem')
        return getattr(self,item)

class JSONEncoder(_JSONEncoder):

    def default(self,o):
        super().default(o)
        return dict(o)




class Flask(_Flask):
    json_encoder = JSONEncoder

app = Flask(__name__)

@app.route('/index')
def f():


    return jsonify(A())

# dict










# obj = A()
# print(dict(obj))
app.run(host='0.0.0.0',port='9999')
