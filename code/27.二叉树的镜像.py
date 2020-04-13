# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
########### 递归法
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return
        if not root.left and not root.right: return root
        root.left, root.right = root.right, root.left
        if root.left:
            self.mirrorTree(root.left)
        if root.right:
            self.mirrorTree(root.right)
        return root