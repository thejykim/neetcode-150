class Solution:
    def solve(self, board: List[List[str]]) -> None:
        safe = set()

        def dfs(x: int, y: int):
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
                return
            
            if (x, y) in safe:
                return
            
            if board[x][y] != 'O':
                return
            
            safe.add((x, y))

            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        rows, cols = len(board), len(board[0])

        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                    dfs(i, j)
        
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if (i, j) not in safe:
                    board[i][j] = 'X'
        