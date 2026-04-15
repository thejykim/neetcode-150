class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res, queens = [], []

        def validPosition(x: int, y: int) -> bool:
            for queen in queens:
                r, c = queen
                if r == x or c == y:
                    return False
                
                if r + c == x + y or r - c == x - y:
                    return False
            return True
        
        def answer() -> List[List[str]]:
            space = ['.' * n for _ in range(n)]
            
            for queen in queens:
                r, c = queen
                space[r] = '.' * c + 'Q' + '.' * (n - c - 1)
            
            return space
        
        def backtrack(row: int):
            if row == n:
                res.append(answer())
                return
            
            for col in range(n):
                if validPosition(row, col):
                    queens.append([row, col])
                    backtrack(row + 1)
                    queens.pop()
        
        backtrack(0)
        return res