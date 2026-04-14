import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        
        def quickselect(l, r):
            pivot_index = random.randint(l, r)
            nums[pivot_index], nums[r] = nums[r], nums[pivot_index]
            pivot = nums[r]

            i = l
            for j in range(l, r):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            
            nums[r], nums[i] = nums[i], nums[r]

            if i == target:
                return nums[i]
            elif i < target:
                return quickselect(i + 1, r)
            else:
                return quickselect(l, i - 1)
    
        return quickselect(0, len(nums) - 1)