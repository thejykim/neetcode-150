class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        window = set()

        for r in range(len(nums)):
            if nums[r] in window:
                return True
            
            window.add(nums[r])

            if len(window) > k:
                window.remove(nums[l])
                l += 1
        
        return False