### 递归法
def maxDepth(self, root: TreeNode) -> int:
    if not root: return 0
    return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

###循环法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 循环法，用队列实现,相当于层次遍历
        if not root: return 0
        queue = [root]
        depth = 0
        while queue:
            temp = []
            for node in queue:
                if node.left: temp.append(node.left)
                if node.right: temp.append(node.right)
            queue = temp
            depth += 1

        return depth