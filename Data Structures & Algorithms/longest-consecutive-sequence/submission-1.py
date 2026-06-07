class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        parent = {num: num for num in nums}
        size = {num: 1 for num in nums}

        def find(a: int) -> int:
            while a != parent[a]:
                a = parent[a]
            return a
        
        def union(a: int, b: int):
            a, b = find(a), find(b) # roots
            if a == b:
                return
            
            if size[a] < size[b]:
                a, b = b, a
            
            parent[b] = a
            size[a] += size[b]
        
        for num in nums:
            if num + 1 in parent:
                union(num, num + 1)
        
        return max(size.values()) if size else 0