#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/04 04:16:24 by samui>

import webapp2
from functools import wraps
import logging
from basecontroller import BaseHandler
from base import BaseTemplate
# Model
from google.appengine.ext import db
from article import Article
from comment import Comment


class HelloWebApp2(BaseHandler):
    def get(self):
        template_values = {
            'test':'HelloWorld,WebApp2!',
            #'debug': self.uri_for('home'),
            'debug':'t',
            'uri_for':self.uri_for,
        }
        view = BaseTemplate.render('template/index.html',template_values)
        self.response.write(view)

class Home:
    class Home(BaseHandler):
        def get(self):
            
            template_values = {}
            view = BaseTemplate.render('template/home/index.html',template_values)
            self.response.write(view)


    class View(BaseHandler):
        def get(self,ID = None):
            if ID == None:
                self.redirect_to('home')
            blog = Article.get_by_id(long(ID))
            template_values = {
                'blog': blog,
            }
            view = BaseTemplate.render('template/home/view.html',template_values)
            self.response.write(view)

