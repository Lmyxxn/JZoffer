class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        #法2 进阶版，代码重用性更好，为功能扩展提供便利,可以修改isodd函数，实现不同的判断功能
        i = 0
        j = len(nums) - 1
        while i < j:
            if not self.isOdd(nums[i]) and self.isOdd(nums[j]):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            elif not self.isOdd(nums[i]) and not self.isOdd(nums[j]):
                j -= 1
            elif self.isOdd(nums[i]) and self.isOdd(nums[j]):
                i += 1
            else:
                i += 1
                j -= 1
        return nums

    def isOdd(self, n):
        return n & 1 == 1