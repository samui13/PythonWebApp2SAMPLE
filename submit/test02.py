#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/03 00:48:40 by samui>

import webapp2
import jinja2
import os
import cgi
import handler

app = webapp2.WSGIApplication([
    webapp2.Route(r'/', handler=handler.HelloWebApp2, name='home'),
    webapp2.Route(r'/postA', handler=handler.PostTEST, name='postA'),
    webapp2.Route(r'/postB', handler=handler.PostTEST2, name='postB'),],debug=True)


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
