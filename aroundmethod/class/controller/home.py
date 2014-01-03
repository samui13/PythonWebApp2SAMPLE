#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/03 23:30:54 by samui>

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
        }
        #self.res
        #logging.debug(os.path.dirname(__file__)+"../../")
        self.response.write(BaseTemplate.render('template/index.html',template_values))

