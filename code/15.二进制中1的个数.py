#n与n-1做位与运算可以将最后一个1消去，所以当n不等于0时，n = n&(n-1),count+=1
#需要注意的是，python中负数并不是用补码表示的，所以需要讲它先转换成补码，n = n & 0xffffffff即可
class Solution:
    def hammingWeight(self, n: int) -> int:
        if n < 0:
            n = n & 0xffffffff
        count = 0
        while n:
            count += 1
            n = (n-1)&n
        return count
