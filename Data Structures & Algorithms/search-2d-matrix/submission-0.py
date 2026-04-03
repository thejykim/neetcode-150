class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        lo, hi = 0, m * n - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            row, col = mid // n, mid % n
            curr = matrix[row][col]

            if curr == target:
                return True
            elif curr < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return False