#数字范围为1～n
def getDuplication(nums, n):
    if nums == []: return -1
    for i in range(n+1):
        if nums[i] > n:
            return -1
    #二分法,左闭右闭
    start = 1
    end = len(nums)-1
    while start <= end:
        mid = start + (end-start)//2
        count = countRange(nums, start, mid)
        if start == end:
            if count > 1:
                return start
            else:
                break
        if count > mid-start+1:
            end = mid
        else:
            start = mid +1
    return -1

def countRange(nums, start, end):
    if len(nums) == 0: return 0
    count = 0
    for i in range(len(nums)):
        if nums[i] >= start and nums[i] <= end:
            count +=1
    return count

print(getDuplication([1,1,2,2,3,4],5))
print(getDuplication([1,2,3,4,5,6],5))
print(getDuplication([],5))










