#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/03 05:35:04 by samui>


import webapp2
import jinja2
import os
import cgi
import handler

app = webapp2.WSGIApplication([
    webapp2.Route(r'/', handler=handler.HelloWebApp2, name='home'),
],debug=True)


def main():
    app.run()
if __name__ == '__main__':
    main()

