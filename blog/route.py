#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/04 02:51:03 by samui>


import webapp2
#import jinja2
#import os
#import cgi
import handler

app = webapp2.WSGIApplication([
    webapp2.Route(r'/', handler=handler.HelloWebApp2, name='home'),
    webapp2.Route(r'/session/login',handler=handler.Session.Login,name='login'),
    
    webapp2.Route(r'/my/settings', handler=handler.MyMethod.Setting, name='my_setting'),
    webapp2.Route(r'/my/edit', handler=handler.MyMethod.Edit, name='my_edit'),
    webapp2.Route(r'/my/create', handler=handler.MyMethod.Create, name='my_create'),
    webapp2.Route(r'/my/list', handler=handler.MyMethod.List, name='my_list'),
],debug=True)


def main():
    logging.getLogger().setLevel(logging.DEBUG)
    webapp.util.run_wsgi_app(app)

    #app.run()
if __name__ == '__main__':
    main()

