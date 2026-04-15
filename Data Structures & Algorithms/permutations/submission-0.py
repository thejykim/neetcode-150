class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []
        used = [False] * len(nums)

        def backtrack():
            if len(subset) == len(nums):
                res.append(subset[:])
                return

            for i in range(0, len(nums)):
                if used[i]:
                    continue
                
                subset.append(nums[i])
                used[i] = True
                backtrack()
                used[i] = False
                subset.pop()
        
        backtrack()
        return res