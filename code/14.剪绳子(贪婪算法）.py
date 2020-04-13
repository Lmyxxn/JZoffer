class Solution():
    def __init__(self,n):
        self.n = n
    def cuttingRope(self, n: int) -> int:
        if n < 2: return 0
        if n == 2: return 1
        if n== 3: return 2
        max = 1
        # 贪婪算法就是当绳子长度等于4时，对半剪最大；当绳子长度大于等于5时，每次剪出一段长为3的最好，贪婪算法还不太理解
        while n >= 5:
            max = 3*max
            n -= 3
        max *= 4
        return max
n = 10
s = Solution(n)
print(s.cuttingRope(n))