### 中心扩散法，核心是双指针，遍历一次字符串数组，时间复杂度o(n*n),空间o(1），labuladong的算法小抄里面的，讲得很好

class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = list(s)
        n = len(s)
        res = []
        for i in range(n):
            s1 = self.Palindrome(i, i, s)
            s2 = self.Palindrome(i, i + 1, s)
            if len(res) < len(s1): res = s1
            if len(res) < len(s2): res = s2
        return ''.join(res)

    def Palindrome(self, left, right, s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
