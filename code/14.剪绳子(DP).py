class Solution():
    def __init__(self,n):
        self.n = n
    def cuttingRope(self, n: int) -> int:
        if n < 2: return 0
        if n == 2: return 1
        if n== 3: return 2
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        for j in range(4,n+1):
            for i in range(1,j//2+1):
                dp[j] = max(dp[j], dp[i]*dp[j-i])
        return dp[-1]

n = 10
s = Solution(n)
print(s.cuttingRope(n))