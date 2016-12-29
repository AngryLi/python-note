#!/usr/local/bin/python3 Python

def bubble(no_sorted_list):
    """
    冒泡排序
    :param no_sorted_list: 未排序的列表,必须是list/tuple
    :return:
    """
    run_loop = 0
    if isinstance(no_sorted_list, list):
        sorting_list = no_sorted_list
        for index in range(0, sorting_list.__len__()):
            for j in range(0, sorting_list.__len__() - index - 1):
                run_loop += 1
                if sorting_list[j] < sorting_list[j + 1]:
                    sorting_list[j], sorting_list[j + 1] = sorting_list[j + 1], sorting_list[j]
                    run_loop += 3
    return run_loop

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



