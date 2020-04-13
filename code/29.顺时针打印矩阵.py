
#这个方法不断翻转matrix，每次取第一行。时间长

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            result += matrix.pop(0) ##### 这个地方容易写成.append
            if not matrix: break
            matrix = self.turn(matrix)
        return result

    def turn(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        new_matrix = []
        for j in range(n-1, -1, -1): #这里倒序遍历记住！从n-1开始
            new_row = []
            for i in range(m):
                new_row.append(matrix[i][j])
            new_matrix.append(new_row)
        return new_matrix

#第二种方法剑指offer的方法，还未看