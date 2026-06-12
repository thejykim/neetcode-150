class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo, hi = max(weights), max(weights) * math.ceil(len(weights) / days)
        res = hi

        def total(capacity):
            days_spent = 1
            day_total = 0

            for weight in weights:
                if day_total + weight > capacity:
                    days_spent += 1
                    day_total = weight

                    if days_spent > days:
                        return False
                else:
                    day_total += weight
            
            return True

        while lo <= hi:
            mid = (lo + hi) // 2

            if total(mid):
                res = min(res, mid)
                hi = mid - 1
            else:
                lo = mid + 1

        return res