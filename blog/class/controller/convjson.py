#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/04 05:03:16 by samui>
import webapp2
import logging
import jinja2
from basecontroller import BaseHandler
from base import BaseTemplate
# Model
from google.appengine.ext import db
from article import Article
from comment import Comment


class Json:
    temp ="{"+\
        "'ID':'{{id}}',"+\
        "'title': '{{title}}'," +\
        "'text':'{{text}}'," +\
        "'created_at':'{{created_at}}'" +\
        "}"

    class List(BaseHandler):
        def get(self):
            articles = db.GqlQuery("SELECT * FROM Article ORDER BY created_at DESC limit 10")
            template = jinja2.Template(Json.temp)
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
            #self.response.write("[{'title':'Sample'},{'title':'Sample2'}]")

class Xml:
    class List(BaseHandler):
        def get(self):
            self.response.write("H")
            
