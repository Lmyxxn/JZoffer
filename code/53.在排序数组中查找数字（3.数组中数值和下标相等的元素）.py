### 左闭右闭，其实就是前面的搜索元素
def serchindex(nums):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = left + (right-left)//2
        if nums[mid] == mid:
            return mid
        elif nums[mid] < mid:
            left = mid + 1
        elif nums[mid] > mid:
            right = mid - 1
    return -1

if __name__ == '__main__':
    nums = [-3,-2,1,3,4]
    print(serchindex(nums))