# 问题
在写字典dict => object的函数dict2object时，代码如下：
```
def dict2object(d):
    if '__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        class_ = getattr(module, class_name)
        args = dict((key, value) for key, value in d.items())
        inst = class_(**args)
    else:
        inst = d
    return inst
```
如果传入的实参是一个iterable的对象，函数成功运行，如果传入的对象不可便利，就会在`if '__class__' in d:`处 __raise TypeError__。

因此需要在执行 `in` 之前判断是否可便利。然而python并没有提供函数或则方法判断是否可便利。

# 判断可便利
## 利用 __iter__内建属性
```
if hasattr(obj, '__iter__') :
    print 'iterable'
```
这种方法不能检测字符串，如：`hasattr('', '__iter__')`返回False。
  或者这样子：
```
try :
    i = iter(obj)
except TypeError, v :
    print v
```

## 假设obj是iterable的，如果不是的话，就抛出异常
```
try:
    for v in obj:
        print v
except TypeError, e:
    print e
```

## 检查实例是否是collections.Iterable子类
```
import collections
if isinstance(obj, collections.Iterable):
    print 'iterable'
```
