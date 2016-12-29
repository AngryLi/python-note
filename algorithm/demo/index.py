nums = [1, 390, 90, 4 ,5 ,6 ,1 ,2]
# 快速排序
def sort_quick(need_sort_list : list):
    if need_sort_list.__len__() == 1 or need_sort_list.__len__() == 0:
        return need_sort_list
    else:
        base_num = need_sort_list[0]
        i = 0; j = need_sort_list.__len__() - 1
        while i != j:
            while need_sort_list[j] >= base_num and i < j:
                j -= 1
            while need_sort_list[i] <= base_num and i < j:
                i += 1
            if i < j:
                need_sort_list[i], need_sort_list[j] = need_sort_list[j], need_sort_list[i]
        need_sort_list[0], need_sort_list[i] = need_sort_list[i], base_num
        return sort_quick(need_sort_list[0:i]) + [need_sort_list[i]] + sort_quick(need_sort_list[i+1:need_sort_list.__len__()])
# 冒泡排序
def sort_pipple(need_sort_list : list):
    for j in range(0, need_sort_list.__len__() - 2):
        for i in range(j+1, need_sort_list.__len__()-1):
            if need_sort_list[i - 1] > need_sort_list[i]:
                need_sort_list[i - 1], need_sort_list[i] = need_sort_list[i], need_sort_list[i - 1]

sort_pipple(nums)
print(nums)
