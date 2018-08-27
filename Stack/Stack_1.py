#encoding='utf-8'
from pythonds.basic.stack import Stack

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

def check(dataString):
    s = Stack()
    balanced = True
    index = 0

    while index < len(dataString) and balanced:
        data = dataString[index]
        if data in "([{":
            s.push(data)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,data):
                    balanced = False
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False
print(check('{{]]{{{'))
print(check('[{()]'))