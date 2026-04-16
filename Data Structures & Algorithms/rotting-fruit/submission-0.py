from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh_fruit = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_fruit += 1
                elif grid[i][j] == 2:
                    queue.append((i + 1, j))
                    queue.append((i, j + 1))
                    queue.append((i - 1, j))
                    queue.append((i, j - 1))
        
        tick = 0

        while queue:
            rotted = False

            for _ in range(len(queue)):
                i, j = queue.popleft()

                if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                    continue
                
                if grid[i][j] != 1:
                    continue
                
                fresh_fruit -= 1
                grid[i][j] = 2
                rotted = True

                queue.append((i + 1, j))
                queue.append((i - 1, j))
                queue.append((i, j + 1))
                queue.append((i, j - 1))

            if rotted:
                tick += 1

        return tick if fresh_fruit == 0 else -1