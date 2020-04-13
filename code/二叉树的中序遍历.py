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
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

    ## 非递归，利用栈实现，遍历到的节点先加入栈，然后遍历左子节点，当左子节点不存在时，出栈，遍历其右子树

    def inorder1(self, root:TreeNode):
        res = []
        stack = []
        if not root: return

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                temp = stack.pop()
                res.append(temp.val)
                root = temp.right
        return res

if __name__ == '__main__':
    root = TreeNode([3,9,20,None,None,15,7])
    s = Solution()
    print(s.inorder(root))



