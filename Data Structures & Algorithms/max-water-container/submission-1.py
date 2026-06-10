class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            left, right = heights[l], heights[r]
            res = max(res, min(left, right) * (r - l))

            if left < right:
                l += 1
            else:
                r -= 1
        
        return res