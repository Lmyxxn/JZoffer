
###### 贪心思想，dp+二分法，时间o(nlogn)，空间o(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return n
        tails = [nums[0]]

        for i in range(1,n):
            if nums[i] > tails[-1]:
                tails.append(nums[i])
                continue

            l, r = 0, len(tails) - 1
            Flag = 0
            while l <= r:
                mid = l + (r-l)//2
                if tails[mid] == nums[i]:
                    Flag = 1
                    break
                elif tails[mid] < nums[i]:
                    l = mid + 1
                elif tails[mid] > nums[i]:
                    r = mid -1
            if Flag == 0:
                tails[l] = nums[i]

        return len(tails)
