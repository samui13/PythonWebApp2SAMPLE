#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/03 00:59:45 by samui>

import webapp2
import jinja2
import os
import cgi
import handler
import logging
config = {}
config['parameter'] = {'foo':'bar'}

def handle_404(request, response, exception):
    logging.exception(exception)
    response.write('Oops! I could swear this page was here!')
    response.set_status(404)


def handle_500(request, response, exception):
    logging.exception(exception)
    response.write('A server error occurred!')
    response.set_status(500)

config['error_handlers'] = {
    404: handle_404,
    500: handle_500,
}
app = webapp2.WSGIApplication([
    webapp2.Route(r'/', handler=handler.HelloWebApp2, name='home'),
    webapp2.Route(r'/postA', handler=handler.PostTEST, name='postA'),
    webapp2.Route(r'/postB', handler=handler.PostTEST2, name='postB'),
    webapp2.Route(r'/testA', handler=handler.TEST, name='postB'),
],
                              debug=True,
                              config=config['parameter'])
#app.error_handlers[404] = handle_404
app.error_handlers = config['error_handlers']


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
