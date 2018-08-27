#encoding='utf-8'

"""输入有序列表"""
def binarySearch(alist,item):

    first = 0
    last = len(alist)-1
    found = False

    while last <len(alist) and not found:
        mid = (first+last)//2

        if alist[mid] == item:
            return True
        else:
            if alist[mid] < item:
                first = mid + 1
            else:
                last = mid - 1
    return False

print(binarySearch([0,1,2,3,4,5,42,56],3))

