#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/03 23:24:05 by samui>

import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)+"/../.."),
    #loader=jinja2.FileSystemLoader("/Users/samui/temp/python/GAE/google_appengine/product/aroundmethod/"),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class BaseTemplate:
    @classmethod
    def render(self, template, params):
        baseTemplate = JINJA_ENVIRONMENT.get_template('template/common/base.html')
        headTempate = JINJA_ENVIRONMENT.get_template('template/common/_header.html')
        footTemplate = JINJA_ENVIRONMENT.get_template('template/common/_footer.html')
        params.update({
            'common_base': baseTemplate.render({'title':'SimpleTitle'}),
            'common_head':headTempate.render({'uri_for':webapp2.uri_for}),
            'common_footer': footTemplate.render({'uri_for':webapp2.uri_for}),
        })
        bodyTemplate = JINJA_ENVIRONMENT.get_template(template)
        return bodyTemplate.render(params)

