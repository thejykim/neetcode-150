class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])

        def backtrack(x: int, y: int, i: int) -> bool:
            if i == len(word):
                return True
            
            if x >= row or y >= col or x < 0 or y < 0:
                return False
            
            if board[x][y] != word[i]:
                return False
            
            temp, board[x][y] = board[x][y], '#'
            found = (backtrack(x + 1, y, i + 1) or backtrack(x, y + 1, i + 1) or
                    backtrack(x - 1, y, i + 1) or backtrack(x, y - 1, i + 1))
            board[x][y] = temp

            return found
        
        for x in range(0, row):
            for y in range(0, col):
                if (backtrack(x, y, 0)):
                    return True

        return False