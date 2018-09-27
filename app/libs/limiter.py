"""
    create by misslove
"""
import functools

from werkzeug.contrib.cache import SimpleCache

__author__ = 'misslove'

class Limiter():
    cache = SimpleCache()
    def limited(self,callback):
        self.callback_limited = callback
        return callback
    def limit(self,key_func=None,key='',time_delta=60):
        def decorate(f):
            key_prefix = 'limiter/'
            @functools.wraps(f)
            def wrapper(*args,**kwargs):
                full_key = key_prefix + key_func() if key_func else key
                value = Limiter.cache.get(full_key)
                if not value:
                    Limiter.cache.set(full_key, time_delta, timeout=time_delta)
                    return f(*args,**kwargs)
                else:
                    return self.callback_limited()
            return  wrapper
        return decorate




