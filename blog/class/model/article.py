#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/04 03:15:59 by samui>


from google.appengine.ext import db
from comment import Comment

class Article(db.Model):
    title = db.StringProperty(required=True)
    #text = db.StringProperty(required=True)
    text = db.TextProperty(required=True)
    comment = db.ReferenceProperty(reference_class=Comment)
    created_at = db.DateTimeProperty(auto_now_add=True)
