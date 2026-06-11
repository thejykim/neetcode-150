class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[i]
            while stack:
                if stack[-1][0] <= temp:
                    stack.pop()
                else:
                    res[i] = stack[-1][1] - i
                    break
            stack.append((temp, i))
        
        return res