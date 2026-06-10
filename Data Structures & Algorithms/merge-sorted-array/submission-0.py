class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2 = m - 1, n - 1
        write = len(nums1) - 1

        while write >= 0:
            if p1 < 0:
                nums1[write] = nums2[p2]
                p2 -= 1
            elif p2 < 0:
                nums1[write] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[write] = nums1[p1]
                p1 -= 1
            else:
                nums1[write] = nums2[p2]
                p2 -= 1
            write -= 1
        
        return