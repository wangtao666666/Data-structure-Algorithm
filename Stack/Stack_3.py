#encoding=utf-8

from pythonds.basic.stack import Stack

def convert(num,base):

    digits = '0123456789ABCDEF'

    stack = Stack()

    while num > 0:
        stack.push(num % base)
        num = num // base

    newString = ''


    while not stack.isEmpty():
        newString = newString + digits[stack.pop()]

    return newString

print(convert(8,2))
