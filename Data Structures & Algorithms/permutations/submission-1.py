class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(index: int):
            if index == len(nums):
                res.append(nums[:])
                return
            
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                backtrack(index + 1)
                nums[i], nums[index] = nums[index], nums[i]
        
        backtrack(0)
        return res