class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        left, right = [0] * length, [0] * length

        max_ = 0
        for i in range(length):
            max_ = max(max_, height[i])
            left[i] = max_
        
        max_ = 0
        for i in range(length - 1, -1, -1):
            max_ = max(max_, height[i])
            right[i] = max_
        
        res = 0
        for i in range(length):
            rain = min(left[i], right[i]) - height[i]
            res += max(0, rain)
        
        return res
