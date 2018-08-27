#encoding=utf-8

from pythonds.basic.queue import Queue

def check(namelist,num):
    queue = Queue()

    """把名单列表里面的名字全部添加到队列中"""
    for name in namelist:
        queue.enqueue(name)

    while queue.size()>1:

        """循环队列定义好某几个数从队列头中进行删除操作，被删除之后添加到队尾中"""
        for i in range(num):
            queue.enqueue(queue.dequeue())

        queue.dequeue()

    return queue.dequeue()

print(check(['songhan','laoliang','dashi','jianfu','xiaoshou','yaoyiyao'],10))
