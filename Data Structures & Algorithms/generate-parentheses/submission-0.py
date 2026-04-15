# at each step we have three decisions:
# 1. start a new set of parenthesis (if available)
# 2. close a set of parenthesis (if available)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []

        def backtrack(opened: int, closed: int):
            if opened == closed == n:
                res.append("".join(subset))
                return

            if opened < n:
                subset.append('(')
                backtrack(opened + 1, closed)
                subset.pop()
            
            if opened > closed:
                subset.append(')')
                backtrack(opened, closed + 1)
                subset.pop()
        
        backtrack(0, 0)
        return res