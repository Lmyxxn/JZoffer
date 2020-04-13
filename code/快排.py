def quick_sort(A):
    start = 0
    end = len(A)-1
    q_sort(A, start, end)
    return A


### 递归法
# def q_sort(A, start, end):
#     if start < end:
#         pivot = partition(A, start, end)
#         partition(A, start, pivot-1)
#         partition(A,pivot+1, end)

### 非递归法
def q_sort(A, start, end):
    stack = []
    stack.insert(0, start)
    stack.insert(0, end)
    while stack:
        left = stack.pop()
        right = stack.pop()
        pivot = partition(A, left, right)
        if left < pivot - 1:
            stack.insert(0, left)
            stack.insert(0, pivot-1)
        if pivot + 1 < right:
            stack.insert(0, pivot+1)
            stack.insert(0, right)






def partition(A, start, end):
    left, right = start, end
    temp= A[left]
    while left < right:
        while left < right and A[right] >= temp:  ### 这里的left < right 很容易忘记写！！！！！！
            right -= 1
        if left < right:
            A[left] = A[right]
            left += 1
        while left < right and A[left] <= temp:  ##都是与temp比大小
            left += 1
        if left < right:
            A[right] = A[left]
            right -= 1
    A[left] = temp ###最后这个不要忘
    pivot = left
    return pivot

A = [3,2,5,9,2]
print(quick_sort(A))





