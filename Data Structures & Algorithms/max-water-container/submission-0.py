class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            left, right = heights[l], heights[r]
            water = (r - l) * min(right, left)
            res = max(res, water)

            if right > left:
                l += 1
            else:
                r -= 1
        
        return res