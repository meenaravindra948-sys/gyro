import heapq

def findKthLargest(nums, k):
    heap = []

    for i in nums:
        heapq.heappush(heap, i)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]

nums = [2,0,2,1,1,0]

print(findKthLargest(nums, 2))