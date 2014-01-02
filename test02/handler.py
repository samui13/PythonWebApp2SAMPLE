#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/02 21:30:19 by samui>
import cgi
import webapp2
import jinja2
import os
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HelloWebApp2(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'test':'HelloWorld,WebApp2!',
            #'debug': self.uri_for('home'),
            'debug':'t',
        }
        template = JINJA_ENVIRONMENT.get_template('template/index.html')
        self.response.write(template.render(template_values))
        
class PostTEST(webapp2.RequestHandler):
    def post(self):
        test = cgi.escape(self.request.get('name'))
        self.response.write("test"+test)


        
