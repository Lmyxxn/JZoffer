# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
####### 剑指offer的做法，画个图就能清晰的明白了，还是用队列，加一个level

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = [root]
        res = [[root.val]]
        level = 1
        while queue:
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            level += 1
            if level%2 == 0:
                res.append([node.val for node in temp][::-1])
            else:
                res.append([node.val for node in temp])
            queue = temp
        return res[:-1]


