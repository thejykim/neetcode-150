class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        def dfs(x: int, y: int) -> int:
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                return 0
            
            if grid[x][y] == 0:
                return 0
            
            grid[x][y] = 0

            return 1 + dfs(x + 1, y) + dfs(x, y + 1) + dfs(x - 1, y) + dfs(x, y - 1)

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    res = max(res, dfs(x, y))
        
        return res