from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        queue = deque()

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    queue.append((x + 1, y))
                    queue.append((x, y + 1))
                    queue.append((x - 1, y))
                    queue.append((x, y - 1))
        
        dist = 1

        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                
                if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                    continue
                    
                if grid[i][j] == INF:
                    grid[i][j] = dist
                    queue.append((i + 1, j))
                    queue.append((i, j + 1))
                    queue.append((i - 1, j))
                    queue.append((i, j - 1))
                
            dist += 1


