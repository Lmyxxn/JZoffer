##### 要记住！

class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode.right:#有右子树
            p=pNode.right
            while p.left:
                p=p.left
            return p
        while pNode.next:#无右子树，则找第一个当前节点是父节点左孩子的节点
            if(pNode.next.left==pNode):
                return pNode.next
            pNode = pNode.next#沿着父节点向上遍历
        return  #到了根节点仍没找到，则返回空