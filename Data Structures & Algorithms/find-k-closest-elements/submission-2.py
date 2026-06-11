class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0

        for r in range(k, len(arr)):
            a, b = arr[l], arr[r]

            if abs(a - x) > abs(b - x):
                l += 1 # :-)
            else:
                if a < b:
                    return arr[l:r]
        
        return arr[l:l + k]