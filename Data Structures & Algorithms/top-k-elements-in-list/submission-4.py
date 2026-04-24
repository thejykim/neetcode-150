import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        res = []

        for key in count:
            if len(res) < k:
                heapq.heappush(res, (count[key], key))
            else:
                heapq.heappushpop(res, (count[key], key))

        return [key for (_, key) in res]