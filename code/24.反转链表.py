#三个指针：pre、cur、temp
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return
        pre = None #初始时定义pre为None
        cur = head
        while cur.next:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        cur.next = pre
        return cur