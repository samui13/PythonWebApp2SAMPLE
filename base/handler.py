#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/03 00:30:01 by samui>
import cgi
import webapp2
import jinja2
import os
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class BaseHandler(webapp2.RequestHandler):
    def render2(self, template, params):
        baseTemplate = JINJA_ENVIRONMENT.get_template('template/common/base.html')
        params.update({
            'common_head':JINJA_ENVIRONMENT.get_template('template/common/_header.html').render({'uri_for':self.uri_for})
        })
        template = JINJA_ENVIRONMENT.get_template(template)
        return baseTemplate.render(params)+template.render(params)


class HelloWebApp2(BaseHandler):
    def get(self):
        template_values = {
            'test':'HelloWorld,WebApp2!',
            'debug': self.uri_for('home'),
            'uri_for': self.uri_for,
            #'debug':'t',
        }
        #template = JINJA_ENVIRONMENT.get_template('template/index.html')
        self.response.write(self.render2('template/index.html',template_values))
        self.response.write(self.app.config.get('foo'))

class PostTEST2(webapp2.RequestHandler):
    def post(self):
        test = cgi.escape(self.request.get('name'))
        template_values = {
            'test': test,
        }
        template = JINJA_ENVIRONMENT.get_template('template/submit.html')
        self.response.write(template.render(template_values))
        
        
        
class PostTEST(webapp2.RequestHandler):
    def post(self):
        test = cgi.escape(self.request.get('name'))
        self.response.write("test"+test)


        
