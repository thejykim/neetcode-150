from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        result = hi

        while lo <= hi:
            mid = (lo + hi) // 2
            total = self.total(piles, mid)

            if total <= h:
                result = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        return result

    def total(self, piles, k) -> int:
        return sum(ceil(pile / k) for pile in piles)