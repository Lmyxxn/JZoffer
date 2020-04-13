
##### 找出数字出现的左边界、右边界，相减加一即可，时间：o(logn)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = self.searchleft(nums, target)
        right = self.searchright(nums, target)
        if left != -1 and right != -1:
            return right - left + 1
        else:
            return 0

    #### 二分查找寻找左边界 o(logn)
    def searchleft(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid - 1      ##### 如果nums[mid]==target，收紧右边界
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        if left == len(nums) or nums[left] != target:
            return -1
        else:
            return left

    #### 二分查找寻找右边界 o(logn)
    def searchright(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2  ##### 如果nums[mid]==target，收紧左边界
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        if right < 0 or nums[right] != target:
            return -1
        else:
            return right
