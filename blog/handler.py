#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/04 04:34:41 by samui>
import cgi
import webapp2
import jinja2
import os
import logging
from functools import wraps

import sys

# Model
sys.path.append(os.path.dirname(__file__)+"/class/model")
from article import Article
from comment import Comment



sys.path.append(os.path.dirname(__file__)+"/class/controller")
sys.path.append(os.path.dirname(__file__)+"/class/view")
from basecontroller import BaseHandler
from mymethod import MyMethod
from home import HelloWebApp2,Home
from session import Session
from convjson import Json,Xml

#
from controllApp import AroundMethod
