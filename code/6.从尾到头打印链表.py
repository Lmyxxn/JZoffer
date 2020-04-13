#方案一：反转链表，然后按顺序打印（需要更改原始链表，问面试官可以不可以）
#方案二：遍历链表，依次进栈，遍历完依次出栈（推荐）
#方案三：递归，每次遍历一个节点，先输出后一个节点值，再输出此节点值
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        p = listNode
        stack = []
        res = []
        while p:
            stack.append(p.val)
            p = p.next
        for i in range(len(stack)):
            res.append(stack.pop())
        return res

#在牛客上写比较好

