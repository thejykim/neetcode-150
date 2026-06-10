class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1, p2 = 0, len(numbers) - 1

        while p1 <= p2:
            curr = numbers[p1] + numbers[p2]

            if curr == target:
                return [p1 + 1, p2 + 1]
            elif curr < target:
                p1 += 1
            else:
                p2 -= 1
        
        return [1, 2]