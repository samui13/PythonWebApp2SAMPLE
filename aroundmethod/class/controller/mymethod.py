#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/03 23:43:02 by samui>

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
            template_values = {
                'test':'HelloWorldWebApp2!',
                'debug':'t',
            }
            self.response.write("Settings")
            view = BaseTemplate.render('template/index.html',template_values)
            self.response.write(view)

    class Bookmark(BaseHandler):
        #@AroundMethod(before,after)
        def get(self):
            template_values = {
                'test':'HelloWorld,WebApp2!',
                #'debug': self.uri_for('home'),
                'debug':'t',
            }
            view = BaseTemplate.render('template/index.html',template_values)
            self.response.write("Bookmarks")
            self.response.write(view)
            
    Setting.get = AroundMethod(before,after)(Setting.get)
    Bookmark.get = AroundMethod(before,after)(Bookmark.get)
    
