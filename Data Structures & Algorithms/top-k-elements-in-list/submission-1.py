class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()

        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        return sorted(count, key=count.get, reverse=True)[:k]