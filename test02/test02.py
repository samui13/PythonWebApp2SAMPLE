#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/02 21:31:21 by samui>

import webapp2
import jinja2
import os
import cgi
import handler

app = webapp2.WSGIApplication([
    webapp2.Route(r'/', handler=handler.HelloWebApp2, name='home'),
    webapp2.Route(r'/post', handler=handler.PostTEST, name='post'),
],debug=True)


def main():
    app.run()
if __name__ == '__main__':
    main()

"""
def main():
    from paste import httpserver
    httpserver.serve(app,host='127.0.0.2',port='8080')

if __name__ == '__main__':
    main()
"""
