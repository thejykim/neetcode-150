class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(start: int):
            res.append(subset[:])

            for i in range(start, len(nums)):
                subset.append(nums[i])

                backtrack(i + 1)

                subset.pop()
        
        backtrack(0)

        return res