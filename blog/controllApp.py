#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/04 01:43:52 by samui>
from functools import wraps

class AroundMethod(object):
    def __init__(self,before,after):
        self.bFunc = before
        self.aFunc = after
    def __call__(self,callFunc):
        @wraps(callFunc)
        def wrapCall(*args,**kwds):
            try: 
                self.bFunc('')
                r = callFunc(*args,**kwds)
            finally:
                self.aFunc('')
            return r
        return wrapCall

