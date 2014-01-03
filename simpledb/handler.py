#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/04 01:16:29 by samui>
import cgi
import webapp2
import jinja2
import os
import logging

from google.appengine.ext import db
#from model import Comment,Article

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Comment(db.Model):
    text = db.StringProperty(required=True)
    created_at = db.DateTimeProperty(auto_now_add=True)


class Article(db.Model):
    title = db.StringProperty(required=True)
    text = db.StringProperty(required=True)
    comment = db.ReferenceProperty(reference_class=Comment)
    created_at = db.DateTimeProperty(auto_now_add=True)



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


class HelloWebApp2(BaseHandler):
    def get(self):
        """
        p1 = Article(title="SampleTitle0",text="SampleTEXT")
        p1.put()
        """
        #articles = db.GqlQuery("SELECT * FROM Article ORDER BY date DESC LIMIT 10")
        articles = db.GqlQuery("SELECT * FROM Article ORDER BY created_at DESC")
        for blog in articles:
            self.response.write(blog.title+"<br />")
            self.response.write(blog.created_at)
            self.response.write("<br />")
        
        template_values = {
            'test':'HelloWorld,WebApp2!',
            #'debug': self.uri_for('home'),
            'debug':'t',
        }
        view = BaseTemplate.render('template/index.html',template_values)
        self.response.write(view)
