#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import os
import json
import urllib
import time
import datetime
from xml.etree.ElementTree import *
import webapp2
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        smNumber = ((self.request.get('mylistURL')).split('/'))[-1]
        template_values = {
            'nicoRSS':'http://www.nicovideo.jp/mylist/'+smNumber+'?rss=2.0',
            'smNumber':'/json?smNum='+smNumber,
        }
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))
class GetNicoRSS(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(self.request.get('smNum'))

class GetJson(webapp2.RequestHandler):
    def get(self):
          #resp = request.get('http://www.nicovideo.jp/mylist/39252208?rss=2.0')
        #url = 'http://www.nicovideo.jp/mylist/39252208?rss=2.0'
        url = 'http://www.nicovideo.jp/mylist/'+self.request.get('smNum')+'?rss=2.0'
        result = urllib.urlopen(url)
        rss    = fromstring(result.read())
        self.response.headers['Content-Type'] = 'application/json'
        data = []
        for item in rss.getiterator('item'):
            stime = datetime.datetime.strptime(item.findtext('pubDate'), '%a, %d %b %Y %H:%M:%S +0900')
            if stime.year > 2013:
                continue
            
            data.append("{"\
                        '"title":"'+item.findtext('title')+'",'\
                        '"link":"'+item.findtext('link')+'",'\
                        '"guit":"'+item.findtext('guid')+'",'\
                        '"pubDate":"'+item.findtext('pubDate')+'",'\
                        '"Date":"'+str(stime)+'",'\
                        '"Sm":"'+((item.findtext('link').split('/')[-1]).split('sm'))[-1]+'",'\
                        '"month":"'+str(stime.month)+'"'\
                        #'"description":"'+item.findtext('description')+'"'\
                        "}")
            
        
        result = "{\"datas\":["+','.join(data)+"]}";
        self.response.out.write(result)

app = webapp2.WSGIApplication([
    ('/',MainPage),
     ('/sign',GetNicoRSS),
     ('/json',GetJson),
],debug=True)
