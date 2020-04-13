# -*- coding:utf-8 -*-
#### 输入matrix是字符串表示的（牛客上），所以先把matrix变为list，索引的时候用matix[i*cols+j]表示矩阵中的matrix[i][j]
class Solution:
    def __init__(self, matrix, rows, cols, path):
        self.matrix = matrix
        self.rows = rows
        self.cols = cols
        self.path = path

    def hasPath(self, matrix, rows, cols, path):
        # write code here
        matrix = list(matrix)  ###不把matrix变为list的话，下面的matrix[i*cols+j] = '/'这一步就不能进行，因为字符串变量不可修改
        for i in range(rows):
            for j in range(cols):
                if self.dfs(i, j, 0, path, matrix, rows, cols):
                    return True
        return False

    def dfs(self,i, j, k, path, matrix, rows, cols):
        if k == len(path):
            return True
        if not 0 <= i < rows or not 0 <= j < cols or matrix[i * cols + j] != path[k]:
            return False
        temp = matrix[i * cols + j]
        matrix[i * cols + j] = '/'
        res = self.dfs(i + 1, j, k + 1, path, matrix, rows, cols) or self.dfs(i - 1, j, k + 1, path, matrix, rows,
                                                                              cols) or self.dfs(i, j + 1, k + 1, path,
                                                                                                matrix, rows,
                                                                                                cols) or self.dfs(i,
                                                                                                                  j - 1,
                                                                                                                  k + 1,
                                                                                                                  path,
                                                                                                                  matrix,
                                                                                                                  rows,
                                                                                                                  cols)
        matrix[i * cols + j] = temp  ###不要忘了回溯完这个位置，要把它恢复
        return res


matrix="ABCESFCSADEE"
rows=3
cols = 4
path = "ABCCED"

s = Solution(matrix, rows, cols, path)
print(s.hasPath(matrix, rows, cols, path))