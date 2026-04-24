import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []

        for i in range(0, k):
            heapq.heappush_max(heap, (nums[i], i))
        
        res.append(heap[0])

        for i in range(k, len(nums)):
            heapq.heappush_max(heap, (nums[i], i))
            while heap[0][1] <= (i - k):
                heapq.heappop_max(heap)
            
            res.append(heap[0])
        
        return [val for val, _ in res]
