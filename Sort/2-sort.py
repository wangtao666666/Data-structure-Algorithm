#encoding='utf-8'

"""
    短冒泡排序
"""
def shortBubbleSort(alist):
    exchanges = True
    item = len(alist) - 1
    
    while item > 0 and exchanges:
        exchanges = False
        for i in range(item):
            if alist[i] > alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

        item = item -1

    return alist

print(shortBubbleSort([20,30,40,90,50,60,70,80,100,110]))