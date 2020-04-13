# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
########## 用递归的方法做，清晰简单
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B: return False
        result = False
        if A.val == B.val:
            result = self.AHasB(A, B)
        if not result:
            result = self.isSubStructure(A.left, B)
        if not result:
            result = self.isSubStructure(A.right, B)
        return result

    def AHasB(self, A, B):
        if not B:
            return True
        if not A:
            return False
        if A.val != B.val:
            return False
        return self.AHasB(A.left, B.left) and self.AHasB(A.right, B.right)
