import tornado.web
from methods.util import Util

class BaseHandler(tornado.web.RequestHandler):
    def checkKey(self):
        key = self.get_body_argument('key', None)
        if key == Util.Key:
            return True
        return False