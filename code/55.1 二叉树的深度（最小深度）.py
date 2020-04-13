# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


### 递归停止条件要判断好，四种
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        elif not root.left and not root.right: return 1
        elif not root.left: return 1+self.minDepth(root.right)
        elif not root.right: return 1+self.minDepth(root.left)
        else:
            return 1+min(self.minDepth(root.left), self.minDepth(root.right))

### 循环法，用层次遍历，第一个没有孩子节点的节点level就是最小深度
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue = [root]
        level = 1
        while queue:
            temp = []
            for node in queue:
                if not node.left and not node.right:
                    return level
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
            level += 1


