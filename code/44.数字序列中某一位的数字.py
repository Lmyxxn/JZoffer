####根据题目的要求,两个数字m和n能拼接成数字mn和nm,如果mn < nm那么现在他们的相对位置是正确的,如果mn > nm,那么就需要将n移到m的前面,根据这样的特性我们能将整个数组进行排列,得到最终的结果.
####我们在比较的时候先将数据转换成str格式的,利用str格式的字符串直接比较就可以
####这个题目要求我们转换成字符串的形式,是隐含了一个大数的问题

class Solution:
    def findNthDigit(self, n: int) -> int:
        ### 首先判断目标所在的数是几位的，用digits表示
        base = 9
        digits = 1
        while n - base * digits > 0:
            n -= base * digits
            base *= 10
            digits += 1
        idx = n % digits
        number = pow(10, digits - 1)
        if idx == 0:
            target = n // digits + number - 1
            idx = digits
        else:
            target = n // digits + number

        for i in range(idx, digits):
            target = target // 10
        return target % 10





