#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/04 06:00:15 by samui>

import webapp2
import cgi
import logging
from basecontroller import BaseHandler
from base import BaseTemplate
from controllApp import AroundMethod
# Model
from google.appengine.ext import db
from article import Article
from comment import Comment


class MyMethod:
    def before(self):
        logging.debug("Before")
    def after(self):
        logging.debug("after")
    class Setting(BaseHandler):
        #@AroundMethod(MyMethod.before,MyMethod.after)
        def get(self):
            template_values = {
                'test':'HelloWorldWebApp2!',
                'debug':'t',
                'uri_for':self.uri_for,
            }
            self.response.write("Settings")
            view = BaseTemplate.render('template/index.html',template_values)
            self.response.write(view)
    class Edit(BaseHandler):
        def get(self,ID = None):
            blog = Article.get_by_id(long(ID))
            logging.debug(blog)
            if blog!=None:
                title = blog.title
                text = blog.text
                blogid = blog.key().id()
            else:
                title = "BlogTitleSample0"
                text = "BlogTextSample0"
                blogid = 1

            template_values = {
                'uri_for':self.uri_for,
                'blogTitle':title,
                'blogText':text,
                'blogid': blogid,
            }
            view = BaseTemplate.render('template/my/edit.html',
                                       template_values)
            self.response.write(view)
            
    class Create(BaseHandler):
        def post(self,ID = None):
            atitle = cgi.escape(self.request.get('blogTitle'))
            atext = cgi.escape(self.request.get('blogText'))
            blog = Article(title=atitle,
                           text=atext)
            blog.put()
            #self.response.write(title)
            #self.response.write(atext)
            self.redirect_to('home')

    class Delete(BaseHandler):
        def get(self,ID=None):
            blog = Article.get_by_id(long(ID))
            blog.delete()
            self.redirect_to('my_list')

    class List(BaseHandler):
        #@AroundMethod(before,after)
        def get(self):
            articles = db.GqlQuery("SELECT * FROM Article ORDER BY created_at DESC limit 10")
            template_values = {
                'articles': articles,
            }
            view = BaseTemplate.render('template/my/list.html',template_values)
            self.response.write(view)
            
    Setting.get = AroundMethod(before,after)(Setting.get)
    Create.post = AroundMethod(before,after)(Create.post)
    List.get = AroundMethod(before,after)(List.get)
    #Bookmark.get = AroundMethod(before,after)(Bookmark.get)
    
