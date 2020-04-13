def insert_sort(nums):
    n = len(nums)
    for i in range(1,n):
        index = i
        for j in range(i)[::-1]:
            if nums[index] < nums[j]:
                nums[index], nums[j] = nums[j], nums[index]
                index = j
    return nums

nums = [1,6,3,4,2,5,1]
print(insert_sort(nums))


