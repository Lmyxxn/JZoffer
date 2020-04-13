# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None




class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ## 法1，时间复杂度o(min(m,n)),空间o(m+n)
        head0 = ListNode(0)
        l = head0

        p1 = l1
        p2 = l2
        if not l1:
            return l2
        if not l2:
            return l1
        while l1 and l2:
            if l1.val < l2.val:
                l.next = l1
                l1 = l1.next
            else:
                l.next = l2
                l2 = l2.next
            l = l.next

        if l1:
            l.next = l1
        if l2:
            l.next = l2
        return head0.next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 法2：递归解法，不太好写，时间复杂度o(min(m,n))
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


