## 法2 将带删除节点下一个节点的值复制到这个节点，然后删除下个节点即可，牛客 leetcode都没有JZoffer的这道原题，平均时间o(1)，空间o(1)
class Solution:
    def deleteNode(self, head, val):
        if head is None or val is None:
            return None
        if val.next is not None:  # 待删除节点不是尾节点
            tmp = val.next
            val.val = tmp.val
            val.next = tmp.next
        elif head == val:  # 待删除节点只有一个节点，此节点为头节点
            head = None
        else:
            cur = head    # 待删除节点为尾节点,这个时候就需要从头遍历了
            while cur.next != val:
                cur = cur.next
            cur.next = None
        return head

    #法1：从头遍历，时间o(n)，leetcode面试题18，这里给出待删除的节点类型是int

    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None

    class Solution:
        def deleteNode(self, head: ListNode, val: int) -> ListNode:
            # 法1，时间o(n),空间o(1)
            dummy = ListNode(0)
            dummy.next = head
            if dummy.next.val == val: return head.next
            while head and head.next:
                if head.next.val == val:
                    head.next = head.next.next
                    return dummy.next  ## 易错,容易写成head，要记住head是个指针，已经去后面了
                head = head.next
