## 从0-n-1中找最小值与0交换；1-n-1中找最小值与1交换。。。
def select_sort(nums):
    n = len(nums)
    for i in range(n-1):
        index = i
        for j in range(i+1,n):
            if nums[j] < nums[index]:
                index = j
        nums[i], nums[index] = nums[index], nums[i]
    return nums

nums = [2,5,3,4,6,8,3]
print(select_sort(nums))