#!/usr/local/bin/python3 Python
# coding:utf-8

import os
from url import url;

import tornado.web;

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path= os.path.join(os.path.dirname(__file__), 'statics'),
    debug=True,
)

application = tornado.web.Application(
    handlers=url,
    **settings
)
