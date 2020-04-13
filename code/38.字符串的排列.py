
##### 回溯+剪枝法
class Solution:
    def permutation(self, s: str) -> List[str]:
        s = [i for i in s]
        s.sort()
        self.res = []
        self.backtrack([], s)  ###这题index没用，可以省去，因为是看s剪枝的
        return self.res

    def backtrack(self, sol, s):
        if not s:
            self.res.append(''.join(sol))
            return
        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1]:
                continue
            self.backtrack(sol + [s[i]], s[:i] + s[i + 1:])





