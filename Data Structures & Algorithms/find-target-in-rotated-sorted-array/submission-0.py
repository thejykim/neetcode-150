class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        
        if nums[lo] <= target and nums[-1] >= target:
            lo, hi = lo, len(nums) - 1
        else:
            lo, hi = 0, lo - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return -1