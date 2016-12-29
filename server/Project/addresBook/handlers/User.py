from handlers.BaseHandler import BaseHandler

import json
from methods.util import Util


class UserBaseHandler(BaseHandler):
    def _readUserData(self):
        try:
            path = self.get_template_path() + '/' + 'user.json'
            f = open(path)
            jsonStr = ""
            for line in f:
                jsonStr += line
            jsondict = json.loads(jsonStr)
            self.write(jsondict)
        except Exception as e:
            print("出错了")
            print(e)
            self.write_error(404,reason="内部错误")
        finally:
            f.close()


class CreateUser(BaseHandler):
    def post(self, *args, **kwargs):
        try:
            username = self.get_body_argument(name='username')
            password = self.get_body_argument(name='password')
            userid = Util.guid()
            partment = self.get_body_argument(name='partment')
            email = self.get_body_argument(name='email')
            tel = self.get_body_argument(name='tel')
            tag = self.get_body_argument(name='tag')
            creater = self.get_body_argument(name='creater')
            try:
                path = self.get_template_path() + '/' + 'user.json'
                print(path)
                f = open(path,'r+')
                jsonStr = ""
                for line in f:
                    jsonStr += line
                jsonArray = list(json.loads(jsonStr))
                jsonArray.append(
                    {
                        'username': username,
                        'password': password,
                        'userid': userid,
                        'partment': partment,
                        'email': email,
                        'tel': tel,
                        'tag': tag,
                        'creater': creater
                    })
                f.truncate()
                f.write(json.dumps(jsonArray, indent=1))
            except Exception as e:
                print("出错了")
                print(e)
                self.write({
                    "code":500,
                    "reason":"内部错误"
                })
            finally:
                f.close()
        except Exception as e:
            self.write({
                "status":False,
                'reason':'缺少参数'
            });


class GetUserHandler(BaseHandler):
    def post(self, *args, **kwargs):
        if not self.checkKey():
            self.set_status(401, reason='No Authority')
            self.write({"code":401, "resason":'使用了没有鉴权的key'})
        else:
            partment = self.get_body_argument('partment', None)
            try:
                path = self.get_template_path() + '/' + 'user.json'
                f = open(path)
                jsonStr = ""
                for line in f:
                    jsonStr += line
                jsonArray = json.loads(jsonStr)
                results = []
                for user in jsonArray:
                    if user.get('partment') == partment:
                        results.append(user)
                self.set_status(200,reason='ok')
                self.write({"data":results})
            except Exception as e:
                print("出错了")
                print(e)
                self.set_status(404,reason='inner error')
                self.write_error(404, reason="内部错误")
            finally:
                f.close()
import os
import sqlite3

if __name__ == '__main__':
    path = "/Users/Liyazhou/Desktop/Projections/M/note/python/server/Project/addresBook/templates/user.json"
    print(path)
    f = open(path,'r+')
    jsonStr = ""
    for line in f:
        jsonStr += line
    jsonArray = list(json.loads(jsonStr))
    jsonArray.append(
        {
            'username': "李亚洲"
        })
    print(jsonArray)
    print(json.dumps(jsonArray, indent=1))
    f.truncate()
    # f.write(json.dumps(jsonArray, indent=1))
    f.close()
