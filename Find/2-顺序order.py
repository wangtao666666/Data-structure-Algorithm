#encoding='utf-8'

def ordersequenceSearch(data_list,item):
    pos = 0
    found = False

    while pos < len(data_list) and not found:
        if data_list[pos] == item:
            return True
        elif data_list[pos] > item:
            return False
        else:
            pos = pos + 1

    return False
print(ordersequenceSearch([1,2,3,4,5,7,8,10],9))