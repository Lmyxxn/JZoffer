#摩尔投票法： 核心理念为 “正负抵消” 。时间复杂度为 O(N) ，空间复杂度为 O(1) 。是本题的最佳解法。当发生正负抵消时，剩余数组的众数一定不变
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp = nums[0]
        vote = 1
        for i in range(1, len(nums)):
            if nums[i] == temp:
                vote += 1
            else:
                vote -= 1
                if vote == 0:
                    temp = nums[i]
                    vote = 1
        return temp



## 基于快排法
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ###### 基于快排里面的partition函数，时间o(n),空间o(1),leetcode虽超时，面试好用
        start = 0
        end = len(nums)-1
        index = self.partition(nums, start, end)
        while index != len(nums)//2:
            if index > len(nums)//2:
                index = self.partition(nums, start, index-1)
            else:
                index = self.partition(nums, index+1, end)
        return nums[index]

    def partition(self, nums, start, end):
        left, right = start, end
        temp = nums[left]
        while left < right:
            while left < right and nums[right] >= temp:
                right -= 1
            if left < right:
                nums[left] = nums[right]
                left += 1
            while left < right and nums[left] <= temp:
                left += 1
            if left < right:
                nums[right] = nums[left]
                right -= 1
        nums[left] = temp
        pivot = left
        return pivot




####### 哈希表，时间0（n）空间0（n)，遍历数组，构建哈希表，当dic[num]大于数组长度的一半时，返回这个数
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
                if dic[num] > len(nums) / 2: return num
            else:
                dic[num] = 1








