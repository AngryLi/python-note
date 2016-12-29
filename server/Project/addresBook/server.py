#!/usr/local/bin/python3 Python
# coding:utf-8

import tornado.ioloop
import tornado.options
import tornado.httpserver

from application import application

from tornado.options import define, options

define('port', default=8000, help='run on thie given port', type=int)


def main():
    tornado.options.parse_command_line()
    tornado.options.options.logging = 'debug'
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    # application.listen(port=8000)
    print('development sercer is running at http://127.0.0.1:{port}'.format(port=options.port))
    print('quit the server whic control-c')
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
