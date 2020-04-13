# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 递归法
        if not root: return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if not (left or right):
            return True
        elif not (left and right):
            return False
        else:
            if left.val == right.val:
                return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
            else: return False



#######