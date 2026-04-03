class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = dict()

        for i in range(len(nums)):
            curr = nums[i]
            if curr in mem:
                return [mem[curr], i]
            else:
                mem[target - curr] = i
        
        return [0, 1]