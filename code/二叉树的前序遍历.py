class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
## 递归
    def inorder(self, root:TreeNode):
        if not root:
            return []
        return [root.val] + self.inorder(root.left) + self.inorder(root.right)
### 非递归
    def inorder1(self,root:TreeNode):
        res = []
        stack = []
        while stack or root:
            if root:
                res.append(root.val)
                stack.append(root.right)
                root = root.left
            else:
                root = stack.pop()
        return res


    def inorder2(self, root):
        res = []
        stack = []
        while stack or root:
            if root:
                res.append(root.val)
                stack.append(root.right)
                root =  root.right
            else:
                root = stack.pop()
        return res




    def midorder(self, root):
        res = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                temp = stack.pop()
                res.append(temp.val)
                root = temp.right
        return res



    def backorder(self, root):
        res = []
        stack = []
        while stack or root:
            if root:
                res.append(root.val)
                stack.append(root.left)
                root = root.right
            else:
                root = stack.pop()
        return res