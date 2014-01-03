#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/04 05:22:16 by samui>
import webapp2
import logging
import jinja2
import cgi
from basecontroller import BaseHandler
from base import BaseTemplate
# Model
from google.appengine.ext import db
from article import Article
from comment import Comment


class Json:
    normal ="{"+\
        "'ID':'{{id}}',"+\
        "'title': '{{title}}'," +\
        "'text':'{{text}}'," +\
        "'created_at':'{{created_at}}'" +\
        "}"
    class List(BaseHandler):
        def get(self):

            q = cgi.escape(self.request.get('q'))
            if q == "":
                q = 0
            articles = db.GqlQuery("SELECT * FROM Article ORDER BY created_at DESC limit 10 offset {0}".format(q))
            template = jinja2.Template(Json.normal)
            view = []
            for blog in articles:
                view.append(template.render({
                    'id': blog.key().id(),
                    'title':blog.title,
                    'text':blog.text,
                    'created_at':blog.created_at,
                }))
            
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('[')
            self.response.write(','.join(view))
            self.response.write(']')

    class View(BaseHandler):
        def get(self,ID = None):
            blog = Article.get_by_id(long(ID))
            template = jinja2.Template(Json.normal)
            view = []
            view.append(template.render({
                'id': blog.key().id(),
                'title':blog.title,
                'text':blog.text,
                'created_at':blog.created_at,
            }))
            
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('[')
            self.response.write(','.join(view))
            self.response.write(']')
            

class Xml:
    class List(BaseHandler):
        def get(self):
            self.response.write("H")
            
