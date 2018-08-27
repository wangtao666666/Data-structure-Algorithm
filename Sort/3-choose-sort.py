#encoding='utf-8'

def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionofMax = 0
        for loc in range(1,fillslot+1):
            if alist[loc] > alist[positionofMax]:
                positionofMax = loc

        temp = alist[fillslot]
        alist[fillslot] = alist[positionofMax]
        alist[positionofMax] = temp

    return alist

print(selectionSort([54,26,93,17,77,31,44,55,20]))