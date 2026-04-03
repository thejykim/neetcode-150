from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            while len(stack) > 0:
                if stack[0][0] <= temperatures[i]:
                    stack.popleft()
                else:
                    res[i] = stack[0][1] - i
                    stack.appendleft((temperatures[i], i))
                    break
            # no match
            stack.appendleft((temperatures[i], i))
        
        return res
