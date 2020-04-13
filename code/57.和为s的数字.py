### （数组有序）双指针，一个在前面一个在后面，和等于target时return，和大于target时把后面的指针变小，和小于target时，把前面的指针变大。
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums)-1
        while i < j:
            if nums[i] + nums[j] == target:
                return[nums[i], nums[j]]
            elif nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
        return

###  寻找和为target的所有连续数字序列（序列元素不少于两个），双指针组成的滑动窗口法，初始i=1,j=2 o(n)
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i, j = 1, 2
        res = []
        while i < j and j <= target // 2 + 1:
            sums = sum(list(range(i, j + 1)))
            if sums == target:
                res.append(list(range(i, j + 1)))
                i += 1
                j += 1
            elif sums < target:
                j += 1
            elif sums > target:
                i += 1
        return res
