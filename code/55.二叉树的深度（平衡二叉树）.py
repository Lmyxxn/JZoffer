# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#### 自底向上，时间o(n)（最坏），空间o(n)最坏（退化为链表）
#### 定义一个recur函数，这个函数返回-1（代表不是平衡树）或以这个节点为根节点的树的高度（是平衡树）。
#### 判断以root为根节点的子树是不是二叉平衡树，递归调用recur判断左右子树是不是二叉平衡树，不是的话返回-1，代表这个节点的子树不是二叉平衡树，左右都是的话判断左右子树差是不是小于2，是的话返回这个树的高度，不是的话返回-1.
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.recur(root) != -1

    def recur(self, root):
        if not root: return 0
        left = self.recur(root.left)
        if left == -1: return -1
        right = self.recur(root.right)
        if right == -1: return -1
        return max(left, right) + 1 if abs(left-right) < 2 else -1



