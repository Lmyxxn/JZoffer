
###### 用一个辅助栈helper实现，每次data中有新元素进栈，helper中都存放当前最小值。

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.helper = []


    def push(self, x: int) -> None:
        if len(self.data) == 0:
            self.data.append(x)
            self.helper.append(x)
        else:
            self.data.append(x)
            if x > self.helper[-1]:
                self.helper.append(self.helper[-1])
            else:
                self.helper.append(x)

    def pop(self) -> None:
        if len(self.data) == 0: return
        self.helper.pop()
        return self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.helper[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()