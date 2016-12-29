QQ = [6,3,1,7,5,8,9,2,4]

def encode(need_encode_list : list):
    result = []
    if need_encode_list.__len__() == 1:
        result.append(need_encode_list.__getitem__(0))
        return result
    elif need_encode_list.__len__() == 0:
        return result
    else:
        will_delete = need_encode_list.__getitem__(0)
        need_encode_list.__delitem__(0)
        will_remove = need_encode_list.__getitem__(0)
        need_encode_list.__delitem__(0)
        need_encode_list.append(will_remove)
        result.append(will_delete)
        return result + encode(need_encode_list)

# result = encode(QQ)
# print(result)

import queue
q = queue.Queue(4)
print(q)
q.put(2)
q.put(2)
print(q.not_empty)
