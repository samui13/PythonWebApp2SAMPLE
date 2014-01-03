#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/03 23:29:07 by samui>

import webapp2
from functools import wraps
import logging
from basecontroller import BaseHandler
from base import BaseTemplate

class AroundMethod(object):
    def __init__(self,before,after):
        self.bFunc = before
        self.aFunc = after
    def __call__(self,callFunc):
        @wraps(callFunc)
        def wrapCall(*args,**kwds):
            try: 
                self.bFunc('')
                r = callFunc(*args,**kwds)
            finally:
                self.aFunc('')
            return r
        return wrapCall


class MyMethod:
    def before(self):
        logging.debug("Before")
    def after(self):
        logging.debug("after")
    class Setting(BaseHandler):
        #@AroundMethod(MyMethod.before,MyMethod.after)
        def get(self):
            self.response.write("C")

    class Bookmark(BaseHandler):
        #@AroundMethod(before,after)
        def get(self):
            self.response.write("Bookmarks")
            logging.debug('Error')
    Setting.get = AroundMethod(before,after)(Setting.get)
    Bookmark.get = AroundMethod(before,after)(Bookmark.get)
    
