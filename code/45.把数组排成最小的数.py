####思想：把数组中的数字转化为字符串，两两相加，比较nums[i]+nums[j] 和 nums[j] + nums[i]的大小，小的放在前面，最后''.join(nums)再转化为数字

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        if not nums: return None
        nums = [str(num) for num in nums]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] > nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        return ''.join(nums)
