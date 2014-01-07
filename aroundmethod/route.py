#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/07 01:17:57 by samui>


import webapp2
#import jinja2
#import os
#import cgi
import handler

app = webapp2.WSGIApplication([
    webapp2.Route(r'/', handler=handler.HelloWebApp2, name='home'),
    webapp2.Route(r'/my/settings', handler=handler.MyMethod.Setting, name='my_setting'),
    webapp2.Route(r'/my/bookmarks', handler=handler.MyMethod.Bookmark, name='my_bookmark'),
],debug=True)


def main():
    logging.getLogger().setLevel(logging.DEBUG)
    webapp.util.run_wsgi_app(app)

    #app.run()
if __name__ == '__main__':
    main()

