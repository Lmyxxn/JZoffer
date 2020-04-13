#时间o(n),空间o(1)（因为字符种类数是有限的）
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in s:
            if dic[i] == 1: return i
        return ' '