#####剑指offer的方法，递归，二叉搜索树的后序遍历：最后一个是根节点的值，前面的小于根节点值的是左子树，大于根节点值的是右子树，然后递归判断左右子树是否也是二叉搜索树。
#####首先将前面小于根节点的值全部加入左子树序列，再判断后面是否全部大于根节点的值，加入右子树序列，若后面的不是全部大于根节点，返回False。若满足条件，再递归的判断左右序列是不是二叉搜索树的后序遍历序列。
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder: return True
        left = []
        right = []
        i = 0
        while postorder[i] < postorder[-1]:
                left.append(postorder[i])
                i += 1
        for j in range(i,len(postorder)-1):
            if postorder[j]< postorder[-1]:
                return False
            right.append(postorder[j])
        return self.verifyPostorder(left) and self.verifyPostorder(right)
