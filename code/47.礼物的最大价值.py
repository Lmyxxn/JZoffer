class Solution:
    def maxValue(self, grid) -> int:
        ##### 二维dp，时间o(n*n),空间o(n*n)
        if not grid: return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for i in range(m)]
        dp[0][0] = grid[0][0]
        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]



##### 简化为一维DP,用dp保存一行的值,时间o(n*n),空间o(n)
class Solution:
    def maxValue1(self, grid):
        if not grid: return 0
        m = len(grid)
        n = len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]
        for j in range(1, n):
            dp[j] = dp[j - 1] + grid[0][j]
        for i in range(1, m):
            dp[0] = dp[0] + grid[i][0] ##### 每一行都重新定义dp[0]
            for j in range(1, n):
                dp[j] = max(dp[j], dp[j - 1]) + grid[i][j]
        return dp[-1]