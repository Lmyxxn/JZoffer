class Solution:
    x_Input_Error = False ### 设置全局变量，当输入为0且指数为负数时，全局变量为True 表示出错返回0，与正确的返回分开
    def myPow(self, x: float, n: int) -> float:
        if x == 0 and n < 0:
            x_Input_Error = True
            return 0
        if n < 0:
            res = self.PowUnsignedN(x,-n)
            return 1/res
        return self.PowUnsignedN(x,n)
# 用二分法实现x的n次方，时间复杂度可以减小为log（n)
    def PowUnsignedN(self, x, n):
        if n == 0: return 1
        if n == 1: return x
        result = self.PowUnsignedN(x,n >> 1)### 做位运算更快，右移一位相当于除以二，代替//
        result *= result
        if n & 1 == 1: ### 位运算代替%
            result *= x
        return result
