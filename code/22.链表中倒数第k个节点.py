# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head: return  #####！这一行要加上去，体现代码的鲁棒性！
        head0 = ListNode(0)
        head0.next = head
        fast = head0
        slow = head0
        length = self.listNodeLength(head)
        if k > length: return
        while k > 0:
            fast = fast.next
            k -= 1
        while fast.next:
            slow = slow.next
            fast = fast.next
        return slow.next

    def listNodeLength(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length