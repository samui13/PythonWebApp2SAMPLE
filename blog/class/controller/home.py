#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/04 03:53:18 by samui>

import webapp2
from functools import wraps
import logging
from basecontroller import BaseHandler
from base import BaseTemplate


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
    class View(BaseHandler):
        def get(self,ID = None):
            if ID == None:
                self.redirect_to('home')
            #address_k = db.Key.from_path('Employee', 'asalieri', 'Address', 1) 
            #address = db.get(address_k)
            
            self.response.write(ID)
            
