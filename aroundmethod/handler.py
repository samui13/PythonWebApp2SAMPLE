#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/03 05:49:27 by samui>
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
            'common_base': baseTemplate.render({'title':'SimpleTitle'}),
            'common_head':headTempate.render({'uri_for':webapp2.uri_for}),
            'common_footer': footTemplate.render({'uri_for':webapp2.uri_for}),
        })
        bodyTemplate = JINJA_ENVIRONMENT.get_template(template)
        return bodyTemplate.render(params)


class BaseHandler(webapp2.RequestHandler):
    def auth(self):
        pass


class HelloWebApp2(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'test':'HelloWorld,WebApp2!',
            #'debug': self.uri_for('home'),
            'debug':'t',
        }
        """
        template = JINJA_ENVIRONMENT.get_template('template/index.html')
        self.response.write(template.render(template_values))
        """
        self.response.write(BaseTemplate.render('template/index.html',template_values))
