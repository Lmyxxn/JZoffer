# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
######## 剑指offer递归方法实现，利用前序遍历
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.res = []
        if not root: return []
        self.FindPath(root, sum, [])
        return self.res

    def FindPath(self, root, sum, sol):
        sol.append(root.val)
        sum -= root.val #
        if not root.left and not root.right:
            if sum == 0:
                self.res.append(sol[:])  ##### 注意这里一定要写成append(sol[:])而不是append(sol),否则结果会是[],因为相当于复制一个sol，不复制的话后面sol变化的时候res会变
        else:
            if root.left:
                self.FindPath(root.left, sum, sol)
            if root.right:
                self.FindPath(root.right, sum, sol)
        sum += sol.pop() #


