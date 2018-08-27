#encoding=utf-8
"""
    created on 2018-08-15
    @author:wt
    Description:Queue
"""

class Queue():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()
print(q.size())
q.enqueue(88)
print(q.size())
print(q.dequeue())