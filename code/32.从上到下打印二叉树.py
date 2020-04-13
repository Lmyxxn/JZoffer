# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
######## BFS 用队列实现，简单
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        queue = []
        res = []
        queue.append(root)
        while queue:
            temp = queue.pop(0)
            res.append(temp.val)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return res