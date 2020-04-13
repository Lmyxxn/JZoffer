# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.k = 0
        used = [[False] * cols for i in range(rows)]
        self.dfs(0, 0, threshold, rows, cols, used)
        return self.k

    def dfs(self, i, j, threshold, rows, cols, used):
        ### 停止条件，如果这条路走不通了，return
        if not 0 <= i < rows or not 0 <= j < cols or used[i][j] or self.sum(i) + self.sum(j) > threshold: return
        used[i][j] = True
        self.k += 1
        for direction in self.directions:
            i = i + direction[0]
            j = j + direction[1]
            self.dfs(i, j, threshold, rows, cols, used)

    def sum(self, num):
        res = 0
        while num > 0:
            res += num % 10
            num = num // 10
        return res