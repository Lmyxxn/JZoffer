# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
###### 从上到下按行打印
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = [root]
        res = [[root.val]]
        while queue:
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            res.append([node.val for node in temp])
            queue = temp
        return res[:-1]



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
###### 从下到上按行打印
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = [root]
        res = [[root.val]]
        while queue:
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            res.append([node.val for node in temp])
            queue = temp
        return res[::-1][1:]


