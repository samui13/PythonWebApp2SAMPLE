#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/03 20:22:10 by samui>

import webapp2


class BaseHandler(webapp2.RequestHandler):
    def auth(self):
        pass
