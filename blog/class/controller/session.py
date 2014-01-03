#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/04 02:26:25 by samui>

import webapp2
import cgi
from functools import wraps
import logging
from basecontroller import BaseHandler
from base import BaseTemplate
from controllApp import AroundMethod

class Session:
    def before(self):
        logging.debug("Before")
    def after(self):
        logging.debug("After")
    class Login(BaseHandler):
        def get(self):
            template_values = {}
            view = BaseTemplate.render('template/session/login.html',
                                       template_values)
            self.response.write(view)
        def post(self):
            #test = cgi.escape(self.request.get('name'))
            username = cgi.escape(self.request.get('user'))
            password = cgi.escape(self.request.get('password'))
            self.response.write(username)
            self.response.write(password)
            self.redirect_to('home')
