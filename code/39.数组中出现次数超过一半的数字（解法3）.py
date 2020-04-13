
def majorityElement(nums) :
    ###### 基于快排里面的partition函数，时间o(n),空间o(1),但这种方法修改了输入数组。综合来看还是摩尔投票法更好点
    start = 0
    end = len(nums)-1
    index = partition(nums, start, end)
    while index != len(nums)//2:
        if index > len(nums)//2:
            index = partition(nums, start, index-1)
        else:
            index = partition(nums, index+1, end)
    return nums[index]

def partition(nums, start, end):
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


nums = [1,2,3,2,2,2,5,4,2]
print(majorityElement(nums))