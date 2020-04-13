import heapq
def topKFrequent( nums, k):
    ### 建哈希表
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    #### 建大小为k的小根堆，并调整
    heap = []
    res = []
    Flag = 0
    for i in dic:
        if len(heap) < k:
            heap.append([dic[i], i])
            if len(heap) == k and Flag ==0: #### 初始堆
                heapq.heapify(heap)
                Flag = 1
            res.append(heap)
        if len(heap) == k and Flag ==1:
            if dic[i] > heap[0][0]:
                heap[0] = [dic[i], i]
                heapq.heapify(heap)
                res.append(heap)
    # res = [i[1] for i in heap][::-1]
    return res

#
nums = [5,3,1,1,1,3,5,73,1]
k = 3
print(topKFrequent(nums, k))