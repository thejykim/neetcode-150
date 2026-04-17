class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_subset(houses: List[int]) -> int:
            if len(houses) == 1:
                return houses[0]
            
            # dp[i] = max money robbed from house 0 to i
            dp = [0] * len(houses)

            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, len(houses)):
                dp[i] = max(dp[i - 2] + houses[i], dp[i - 1])
            
            return dp[len(houses) - 1]
        
        s1 = nums[0:-1]
        s2 = nums[1:]

        return max(rob_subset(s1), rob_subset(s2))