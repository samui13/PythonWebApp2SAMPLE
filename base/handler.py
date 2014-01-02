#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/03 05:20:03 by samui>
import cgi
import webapp2
import jinja2
import os
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class BaseTemplate:
    @classmethod
    def render(self, template, params):
        baseTemplate = JINJA_ENVIRONMENT.get_template('template/common/base.html')
        headTempate = JINJA_ENVIRONMENT.get_template('template/common/_header.html')
        footTemplate = JINJA_ENVIRONMENT.get_template('template/common/_footer.html')
        params.update({
            'common_head':headTempate.render({'uri_for':webapp2.uri_for}),
            'common_footer': footTemplate.render({'uri_for':webapp2.uri_for}),
        })
        template = JINJA_ENVIRONMENT.get_template(template)
        return baseTemplate.render(params)+template.render(params)


class BaseHandler(webapp2.RequestHandler):
    def auth(self):
        pass

class HelloWebApp2(BaseHandler):
    def get(self):
        template_values = {
            'test':'HelloWorld,WebApp2!',
            'uri_for': self.uri_for,
            #'debug':'t',
        }
        self.response.write(BaseTemplate.render('template/index.html',template_values))


class PostTEST2(BaseHandler):
    def post(self):
        test = cgi.escape(self.request.get('name'))
        template_values = {
            'test': test,
        }
        template = JINJA_ENVIRONMENT.get_template('template/submit.html')
        self.response.write(template.render(template_values))
        
        
        
class PostTEST(BaseHandler):
    def post(self):
        test = cgi.escape(self.request.get('name'))
        self.response.write("test"+test)

class TEST(BaseHandler):
    def get(self):
        self.abort(404)
        
