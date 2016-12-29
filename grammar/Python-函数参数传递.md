## 引用对象作为函数参数传递
从学习过C系语言的开发者或许都会有这么个疑问：函数参数是值传递还是引用传递。

python不能说是完全的面相对象，但是python和ruby等动态语言，一直宣称"一切皆对象"（这点在JS中保守一点，JS存在普通类型，只有Object才是引用类型。而JS中会对number、string进行相应的转化，具体请查看JS资料）。

python中万物皆对象，引用对象，作为函数参数，引用传值。

```
# 函数定义
class Person(object):
    pass

def printId(s):
    print(id(s))

if __name__ == "__main__":
    # class
    p = Person()
    print(id(p))
    printId(p)
    # number
    n = 9
    print(id(n))
    printId(n)
    # str
    s = "李亚洲"
    print(id(s))
    printId(s)

# 输出结果
4541094040
4541094040
4536338800
4536338800
4540752160
4540752160
```
结果和预期的是一样的：__python中引用对象作为函数参数传值是引用传值的方式__。我看过分析说python是"值传递"的，看这里[Python的函数参数传递：传值？引用？](http://blog.csdn.net/kuanglong2016/article/details/47788471)。分析过程很有道理，但是分析过程无法支撑结论。

我是从iOS转过来的，我相应的想到了oc是怎么处理的，我清楚的记得：基础数据类型是值传递，引用类型是引用传递。也就是引用类型和python的结果是一致的，其理解方式可以参照上面那篇引文（值可变和不可变）。
