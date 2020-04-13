#### 空间换时间 空间o(n)，时间o(n)
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0: return
        res = [1]
        p2, p3, p5 = 0, 0 ,0
        for i in range(1,n):
            r2 = res[p2]*2
            r3 = res[p3]*3
            r5 = res[p5]*5
            res.append(min(r2,r3,r5))

            if res[-1] == r2: p2 += 1 ## 注意这里的条件是，if if if 不能用if elif elif，因为如果有相同的数，是按一个数加进res的
            if res[-1] == r3: p3 += 1
            if res[-1] == r5: p5 += 1
        return res[-1]

##### 另外，判断一个数是不是丑数的方法如下

class Solution:
    def isUglyNumber(self, n: int) -> int:
        if n == 0: return False
        ee = [2,3,5]
        for e in ee:
            while n % e == 0:
                n /= e
        return n == 1



