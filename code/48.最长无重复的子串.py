#### 剑指offer方法，详细笔记在笔记本dp部分 leetcode3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        s = list(s)
        n = len(s)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            Flag = 0
            for j in range(i)[::-1]:
                if s[j] == s[i]:
                    d = i - j
                    if d > dp[i - 1]:
                        dp[i] = dp[i - 1] + 1
                    else:
                        dp[i] = d
                    Flag = 1
                    break
            if Flag == 0:
                dp[i] = dp[i - 1] + 1
        return max(dp)
