#encoding='utf-8'

def bubbleSort(list):
    for item in range(len(list)-1,0,-1):
        print('item:',item)
        for i in range(item):
            print('i:',i)
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
    return list

list = [54,26,93,17,77,31,44,55,20]
print(bubbleSort(list))