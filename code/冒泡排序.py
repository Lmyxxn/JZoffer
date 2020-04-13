def bubble_sort(nums):
    n = len(nums)
    for j in range(n-1,0, -1):
        for i in range(j):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums

nums = [1,4,5,2,6,3]
print(bubble_sort(nums))
