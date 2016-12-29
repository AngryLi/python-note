#!/usr/local/bin/python3 Python

import json

import sort

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'Person Object name : {name}, age: {age}'.format(name=self.name, age = self.age)

def object2dict(object):
    d = {}
    d['__class__'] = object.__class__.__name__
    d['__module__'] = object.__module__
    d.update(object.__dict__)
    return d

def dict2object(d):
    try:
        if '__class__' in d:
            class_name = d.pop('__class__')
            module_name = d.pop('__module__')
            module = __import__(module_name)
            class_ = getattr(module, class_name)
            args = dict((key, value) for key, value in d.items())
            inst = class_(**args)
        else:
            inst = d
    except TypeError as e:
        inst = d
    return inst

def openFile(fileName, mode):
    f = open(fileName,mode=mode)
    print('文件内容 : {fileContent}'.format(fileContent=f.read()))
    # f.truncate()
    f.write('4')
    f.close()

if __name__ == '__main__':
    l = [1,2,3]
    sort.bubble(l)
    print(l)