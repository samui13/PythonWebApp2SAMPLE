#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/04 05:07:36 by samui>


import webapp2
#import jinja2
#import os
#import cgi
import handler

app = webapp2.WSGIApplication([
    #webapp2.Route(r'/', handler=handler.HelloWebApp2, name='home'),
    webapp2.Route(r'/', handler=handler.Home.Home, name='home'),
    webapp2.Route(r'/view/<ID:\d+>', handler=handler.Home.View, name='view'),
    webapp2.Route(r'/json/list.json', handler=handler.Json.List, name='json_list'),
    webapp2.Route(r'/json/view.json/<ID:\d+>', handler=handler.Json.View, name='json_view'),
    webapp2.Route(r'/encode/list.xml', handler=handler.Xml.List, name='xml_list'),
    webapp2.Route(r'/session/login',handler=handler.Session.Login,name='login'),
    
    webapp2.Route(r'/my/settings', handler=handler.MyMethod.Setting, name='my_setting'),
    webapp2.Route(r'/my/edit', handler=handler.MyMethod.Edit, name='my_edit'),
    webapp2.Route(r'/my/create', handler=handler.MyMethod.Create, name='my_create'),
    webapp2.Route(r'/my/list', handler=handler.MyMethod.List, name='my_list'),
    webapp2.Route(r'/my/delete', handler=handler.MyMethod.Delete, name='my_delete'),
],debug=True)


def main():
    logging.getLogger().setLevel(logging.DEBUG)
    webapp.util.run_wsgi_app(app)

    #app.run()
if __name__ == '__main__':
    main()

