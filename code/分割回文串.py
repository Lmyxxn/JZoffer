class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.backtrack([], s)
        return self.res

    def backtrack(self, sol, s):
        if not s:
            self.res.append(sol)
            return
        for i in range(1, len(s) + 1):
            if s[:i] != s[:i][::-1]:
                continue
            self.backtrack(sol + [s[:i]], s[i:])  ##### 注意这里把sol与[s[:i]]相加，实现两个list相加






