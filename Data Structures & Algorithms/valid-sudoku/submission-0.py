class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board[0]))]
        squares = [set() for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]

                if val == '.':
                    continue
                
                sq = (i // 3) * 3 + (j // 3)

                if val in rows[i] or val in cols[j] or val in squares[sq]:
                    return False
                
                rows[i].add(val)
                cols[j].add(val)
                squares[sq].add(val)
        
        return True
