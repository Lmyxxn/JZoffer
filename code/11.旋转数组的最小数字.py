# -*- coding:utf-8 -*-
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            elif nums[mid] == nums[right]:
                right -= 1
        return nums[right]


#这道题我们一直保证right在右边区域内，一直收缩left和right，直到left=right，就可以得到右边区域的第一个数，即最小数字。
#图可参考笔记