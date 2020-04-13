### 编辑距离可以用于比较文本相似度、修改文本等场景中
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1) + 1
        n = len(word2) + 1
        dp = [[0]*n for i in range(m)]
        for i in range(m):
            dp[i][0] = i
        for j in range(n):
            dp[0][j] = j
        for i in range(1,m):
            for j in range(1,n):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1]+1,dp[i-1][j]+1, dp[i][j-1]+1)
        return dp[-1][-1]