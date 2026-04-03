class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mi = float('inf')

        for price in prices:
            profit = max(price - mi, profit)
            mi = min(mi, price)

        return profit