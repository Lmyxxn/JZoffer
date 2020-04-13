#### 二分法，左闭右闭，其实是找左边界的问题，找第一个nums[i] != i 的 i，就是确实的数，如果所有都相等，返回left
def missingNumber(nums):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == mid:
            left = mid + 1
        else:
            right = mid - 1 #收紧right
    #if left == len(nums): return left 这句可省去，因为都是return left
    return left



if __name__ == '__main__':
    nums = [0,1,2,3]
    print(missingNumber(nums))

