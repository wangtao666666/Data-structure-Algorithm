#encoding=utf-8

"""
    created on 2018-08-15
    @author:wt
    @Description:检查是否有回文的情况，例如：roor、sssrrrttrrrsss 等
    
"""

from pythonds.basic.deque import Deque


def check(aString):
    dqueue = Deque()

    """遍历字符串加入到队列中"""
    for ch in aString:
        dqueue.addRear(ch)

    Equal = True

    """最终队列剩下的个数为0或者1为成功"""
    while dqueue.size() > 1 and Equal:
        first = dqueue.removeFront()
        last = dqueue.removeRear()
        """队列前面取一个、后面取一个、如果二者不想等，则不匹配，返回False"""
        if first !=last:
            Equal = False

    return Equal

print(check('lsllslsll'))
print(check('roor'))