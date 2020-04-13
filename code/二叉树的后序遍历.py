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
        return self.inorder(root.left) + self.inorder(root.right)+[root.val]
### 非递归,利用前序遍历变形，中右左，然后res[::-1]即可
    def inorder1(self,root:TreeNode):
        res = []
        stack = []
        while stack or root:
            if root:
                res.append(root.val)
                stack.append(root.left)
                root = root.right
            else:
                root = stack.pop()
        return res[::-1]


