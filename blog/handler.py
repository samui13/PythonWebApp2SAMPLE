#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/04 01:46:42 by samui>
import cgi
import webapp2
import jinja2
import os
import logging
from functools import wraps

import sys
sys.path.append(os.path.dirname(__file__)+"/class/controller")
sys.path.append(os.path.dirname(__file__)+"/class/view")
from basecontroller import BaseHandler

from mymethod import MyMethod
from home import HelloWebApp2
from session import Session

#
from controllApp import AroundMethod
