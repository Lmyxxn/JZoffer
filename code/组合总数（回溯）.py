class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()
        self.backtrack([], 0, target, candidates)
        return self.res

    def backtrack(self, sol, index, target, candidates):
        if target == 0:
            self.res.append(sol)
            return
        if index == len(candidates) or target < candidates[index]:
            return

    ####### 前面都跟39题一样，区别都在for循环内，图在笔记上
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]: continue ## 同一级不能出现相同数字，所以在for循环内部设置约束条件
            self.backtrack(sol+[candidates[i]], i+1, target-candidates[i], candidates) ## 同一个数字不能重复使用，所以选了这个数字之后，下一级的下标从i+1开始