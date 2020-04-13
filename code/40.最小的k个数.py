######### 手写堆，先用前k个数建一个大小为k的最大堆，然后将后面的数依次与堆顶元素比较，若小于堆顶元素，把堆顶换成它，然后对他进行堆调整（heapify(heap, k, 0)）
def getLeastNumbers(arr, k):
    if k > len(arr):
        return arr
    if k == 0:
        return []
    #### 构造heapsize=k的最大堆
    heap = build_max_heap(arr[:k])
    for i in range(k, len(arr)):
        if arr[i] < heap[0]:
            heap[0] = arr[i]
            heap = heapify(heap, len(heap), 0)
    return heap

def heapify(arr, n, i):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if i != largest:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    return arr

def build_max_heap( heap):
    for i in range(len(heap) // 2 - 1, -1, -1):
        heapify(heap, len(heap), i)
    return heap


if __name__ == '__main__':
    arr = [0,0,1,2,4,2,2,3,1,4]
    k = 8
    print(getLeastNumbers(arr, k))



######## 调用库函数的方法 heapq.heapify
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0: return []
        if k > len(arr): return arr
        import heapq
        arr = [-i for i in arr]
        ## 先对arr取负再建最小堆
        heap = arr[:k]
        heapq.heapify(heap)
        for i in range(k,len(arr)):
            if arr[i] > heap[0]:
                heap[0] = arr[i]
                heapq.heapify(heap) ######## 注意这个库函数的用法，只能写成heapq.heapify(heap),不能写成heap = heapq.heapify(heap)！
        heap = [-i for i in heap]
        return heap


######### 剑指做法，基于快速排序里partition函数的方法，这种方法时间o(n)，空间o(1),缺点是修改了输入数组

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == len(arr): return arr
        start = 0
        end = len(arr) - 1
        pivot = self.partition(arr, start, end)
        while pivot != k:
            if pivot > k:
                pivot = self.partition(arr, start, pivot - 1)
            else:
                pivot = self.partition(arr, pivot + 1, end)
        return arr[:k]

    def partition(self, arr, start, end):
        left, right = start, end
        temp = arr[left]
        while left < right:
            while left < right and arr[right] >= temp: ### 这里的left < right 很容易忘记写！！！！！！
                right -= 1
            if left < right:
                arr[left] = arr[right]
                left += 1
            while left < right and arr[left] <= temp:
                left += 1
            if left < right:
                arr[right] = arr[left]
                right -= 1
        arr[left] = temp
        pivot = left
        return pivot



