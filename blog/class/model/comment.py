#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/04 03:02:10 by samui>

from google.appengine.ext import db

class Comment(db.Model):
    text = db.StringProperty(required=True)
    created_at = db.DateTimeProperty(auto_now_add=True)

