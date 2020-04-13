### 简化的dp,时间o(n),空间o(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = nums[0]
        res = temp
        for i in range(1,len(nums)):
            if temp > 0:
                temp += nums[i]
            else:
                temp = nums[i]
            res = max(res, temp)
        return res
