# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre:
            return None
        root = TreeNode(pre[0])
        n = tin.index(root.val)
        root.left = self.reConstructBinaryTree(pre[1:n+1], tin[:n])
        root.right = self.reConstructBinaryTree(pre[n+1:], tin[n+1:])
        return root

pre = {1,2,4,7,3,5,6,8}
tin = {4,7,2,1,5,3,8,6}
print(self.reConstructBinaryTree(pre, tin))