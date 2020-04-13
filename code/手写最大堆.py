# #### 剑指40题；定义一个堆调整函数heapify，他负责调整节点i和其子节点
# def heapify(self, arr, n, i):
#     l = 2*i+1
#     r = 2*i+2
#     largest = i
#     if l < n and arr[l] > arr[largest]:
#         largest = l
#     if r < n and arr[r] > arr[largest]:
#         largest = r
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         self.heapify(arr, n, largest)#### 注意如果节点与其子节点对换了，那么应该继续对对换后的节点向下做调整
#
#
# #### 定义一个建初始堆函数
# def build_max_heap(self, heap):
#     for i in range(len(heap)/2 -1, -1, -1):
#         heapify(heap, len(heap), i)
#
# ### 主函数：堆排序函数
# def heap_sort(self, heap):
#     self.build_max_heap(heap) ## 先建一个初始堆
#     for i in range(len(heap)-1, -1, -1):
#         heap[0], heap[i] = heap[i], heap[0]
#         self.heapify(heap, i, 0)
#     return heap




def heapify(arr, n, i):
    l = 2*i + 1
    r = 2*i + 2
    largest = i
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    return arr


def build_heap(heap):
    heap_size = len(heap)
    for i in range(heap_size//2 -1, -1,-1):
        heapify(heap, heap_size, i)
    return heap

def heap_sort(arr):
    n = len(arr)
    heap = build_heap(arr)
    for i in range(n-1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        heapify(heap,i,0)
    return heap


arr = [1,6,7,3,5,8,3]
print(heap_sort(arr))













