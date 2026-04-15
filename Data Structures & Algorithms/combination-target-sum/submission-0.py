class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(start: int, curr: int):
            if curr == target:
                res.append(subset[:])
                return

            for i in range(start, len(nums)):
                new_curr = curr + nums[i]
                if new_curr > target:
                    continue
                
                subset.append(nums[i])
                backtrack(i, new_curr)
                subset.pop()
        
        backtrack(0, 0)
        return res