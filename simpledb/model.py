#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/04 00:33:35 by samui>

from google.appengine.ext import db


class Comment(db.Model):
    text = db.StringProperty(required=True)
    created_at = db.DateTimeProperty(auto_now_add=True)


class Article(db.Model):
    title = db.StringProperty(required=True)
    text = db.StringProperty(required=True)
    comment = db.ReferenceProperty(reference_class=Comment)
    created_at = db.DateTimeProperty(auto_now_add=True)

