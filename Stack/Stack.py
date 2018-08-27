#encoding=utf-8
"""
    created on 2018-08-14
    @author:wt
    Description:Stack
"""
class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

# s = Stack()
# print(s.isEmpty())
# s.push(4)
# s.push('cat')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.isEmpty())
# s.push(555)
# print(s.pop())
# print(s.pop())
# print(s.size())

# encoding='utf-8'

"""
    created on 2018-08-14
    @author wt
"""
"""
    描述:括号匹配
        可以匹配的括号如：(()()) 、(((())))
        匹配不了的括号如：(((((()) ()))))) (()()(()      
        算法基本思想：构造s为一个栈 传入函数的参数为要查看的括号字符串datastring,遍历字符串，
        如果遇到"("，则加入栈，遇到")"，则pop出一个"(",如果字符串还没遍历完，栈空啦，就说明不匹配
        知道遍历结束

"""
from pythonds.basic.stack import Stack

def check(dataString):
    s = Stack()
    balanced = True
    index = 0

    while index < len(dataString) and balanced:
        data = dataString[index]
        if data == "(":
            s.push(data)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print(check('((()))'))
print(check('((()'))

