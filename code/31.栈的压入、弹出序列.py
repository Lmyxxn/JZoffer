#构造辅助栈helper模拟进出栈过程

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if not pushed or not popped: return True
        helper = []
        for i in range(len(pushed)):
            helper.append(pushed[i])
            while popped and helper and popped[0] == helper[-1]:
                popped.pop(0)
                helper.pop()
        if len(helper) == 0 and len(popped) == 0:
            return True
        else:
            return False
