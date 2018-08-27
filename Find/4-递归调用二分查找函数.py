#encoding='utf-8'

"""
    递归地调用二分查找函数
"""
def binarySearch(alist,item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if alist[mid] == item:
            return True
        else:
            if item < alist[mid]:
                return binarySearch(alist[:mid],item)
            else:
                return binarySearch(alist[mid+1:],item)

print(binarySearch([2,3,4,7,8,10,19,28],9))