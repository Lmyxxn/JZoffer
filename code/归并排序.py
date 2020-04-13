#### 递归实现,就是递归地把左半边merge、右半边merge，然后合并（从头开始比较left和right）

def merge_sort(nums):
    n = len(nums)
    if n == 1: return nums
    mid = n // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    sort = []
    while left and right:
        if left[0] < right[0]:
            sort.append(left.pop(0))
        else:
            sort.append(right.pop(0))
    if left:
        sort += left
    if right:
        sort += right
    return sort


nums = [3,2,5,9,2]
print(merge_sort(nums))
