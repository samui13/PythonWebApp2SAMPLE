#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/07 15:47:24 by samui>
import os
import cgi
import webapp2
import jinja2

class Main(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello! World!")

app = webapp2.WSGIApplication([
    ('/',Main),
],debug=True)

if __name__  == "__main__":
    main()
