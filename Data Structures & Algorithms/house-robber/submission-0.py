class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # dp[i] means the max amount of money to be stolen until house i
        # base case 0 and 1 are nums[0] and max(dp[0], nums[1])
        # dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        
        return dp[len(nums) - 1]