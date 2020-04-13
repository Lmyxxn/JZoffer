# 时间O(N),空间O(1)
def duplicate(nums, n, duplication):
    if len(nums) == 0:return False
    for i in range(n):
        if nums[i] > n-1: return False
    for i in range(n):
        while nums[i] != i:
            if nums[i] == nums[nums[i]]:
                duplication.append(nums[i])
                return True
            nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
    return False

# 测试例子
print(duplicate([1,1,2,4,3], 5, []))
print(duplicate([1,1,2,5,3], 5, []))
print(duplicate([], 5, []))