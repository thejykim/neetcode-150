class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        buckets = [[] for _ in range(len(nums) + 1)]

        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        for num, freq in count.items():
            buckets[freq].append(num)
        
        output = []

        for i in range(len(buckets) - 1, 0, -1):
            output.extend(buckets[i])

            if (len(output) >= k):
                return output[:k]
        
        return output[:k]
