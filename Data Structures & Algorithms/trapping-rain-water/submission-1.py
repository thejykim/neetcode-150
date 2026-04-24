class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_max, right_max = 0, 0
        res = 0

        while l < r:
            if height[l] > height[r]:
                right_max = max(height[r], right_max)
                res += right_max - height[r]
                r -= 1
            else:
                left_max = max(height[l], left_max)
                res += left_max - height[l]
                l += 1
        
        return res
