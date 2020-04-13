### 数组中只有一个数只出现一次，其他都出现两次，用异或^
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a
### 数组中只有两个数只出现一次，其他都出现两次
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        res = 0
        for i in nums:
            res ^= i
        h = 1
        while h&res == 0:
            h <<= 1
        a = 0
        b = 0
        for i in nums:
            if i & h == 0:
                a ^= i
            else:
                b ^= i
        return [a,b]

### 数组中只有一个数字出现一次，其他都出现三次
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            cnt = 0  # 记录当前 bit 有多少个1
            bit = 1 << i  # 记录当前要操作的 bit
            for num in nums:
                if num & bit != 0:
                    cnt += 1
            if cnt % 3 != 0:
                # 不等于0说明唯一出现的数字在这个 bit 上是1
                res |= bit

        return res - 2 ** 32 if res > 2 ** 31 - 1 else res
