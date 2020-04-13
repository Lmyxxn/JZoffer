# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1 = self.getLength(headA)
        l2 = self.getLength(headB)
        distance = l1 - l2
        if distance > 0:
            return self.Go(headA, headB, distance)
        else:
            return self.Go(headB, headA, -distance)

    def Go(self, headA, headB, distance):  ### 假设A比B长,distance >0
        while distance:
            headA = headA.next
            distance -= 1
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA

    def getLength(self, headA):
        l = 0
        while headA:
            headA = headA.next
            l += 1
        return l
