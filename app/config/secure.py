"""
    create by misslove
"""
__author__ = 'misslove'
DEBUG = False
SECRET_KEY = '\x88D\xf09\x91\x07\x98\x89f9\xecJ:U\x17\xc5V\xbe\x8b\xef\xd3\xd8\xd3\xe7\x98*4'
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:111111@localhost:3306/fisher'
SQLALCHEMY_TRACK_MODIFICATIONS  = False

# Email配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = '841191837@qq.com'
MAIL_PASSWORD = 'lvabniqnzenlbdib'
# MAIL_SUBJECT_PREFIX = '[鱼书]'
MAIL_SENDER = '鱼书 <hello@yushu.im>'

#redis配置
# CACHE_TYPE= 'redis',
# CACHE_REDIS_HOST= '127.0.0.1',
# CACHE_REDIS_PORT=6379,
# CACHE_REDIS_DB= '',
# CACHE_REDIS_PASSWORD=''