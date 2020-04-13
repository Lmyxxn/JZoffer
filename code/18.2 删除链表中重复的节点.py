### 如1-2-3-3-4 变为 1-2-4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        head0 = ListNode(0)
        head0.next = head
        pre = head0
        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                temp = cur.val
                while cur and cur.val == temp:
                    cur = cur.next
                pre.next = cur
            else:
                pre = cur
                cur = cur.next

        return head0.next