class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            curr = nums[mid]

            if curr == target:
                return mid
            elif curr < target:
                l = mid + 1
            else:
                r = mid - 1
        
        if r < 0:
            return 0
        else:
            return r + 1