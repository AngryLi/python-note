#!/usr/local/bin/python3 Python
#coding:utf-8

"""
the url structure of website
"""

from handlers.User import CreateUser
from handlers.User import GetUserHandler
from handlers.index.IndexHandler import IndexHandler

url = [
    ('/', IndexHandler),
    ('/user/get', GetUserHandler),
    ('/user/create', CreateUser)
]