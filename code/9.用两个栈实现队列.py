# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        self.stack1.append(node)
        # write code here
    def pop(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        res = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return res

# 两个队列实现一个栈
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, node):
        self.queue1.append(node)
        # write code here

    def pop(self):
        while len(self.queue1)>1:
            self.queue2.append(self.queue1.pop(0))
        res = self.queue1.pop(0)
        while self.queue2:
            self.queue1.append(self.queue2.pop(0))
        return res

