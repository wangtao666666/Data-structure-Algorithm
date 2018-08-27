#encoding='utf-8'

def hash(astring,tablesize):
    sum_data = 0

    for pos in range(len(astring)):
        sum_data = sum_data + ord(astring[pos])

    return sum_data%tablesize