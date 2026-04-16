class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        def dfs(x: int, y: int) -> bool:
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                return False
            
            if grid[x][y] == '1':
                grid[x][y] = '0'

                dfs(x + 1, y)
                dfs(x, y + 1)
                dfs(x - 1, y)
                dfs(x, y - 1)

                return True
            
            return False
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        
        return res