#encoding='utf-8'
"""
    created on 2018-08-20
    @author:wt
"""

def sequenceSearch(alist,item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

        return found

data_list = [2,3,4,5,6,22,33,11,98,0]
print(sequenceSearch(data_list,2))
print(sequenceSearch(data_list,99))