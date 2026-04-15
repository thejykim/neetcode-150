class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        chars = ['+', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res, subset = [], []

        def backtrack(i: int):
            if i == len(digits):
                res.append("".join(subset[:]))
                return

            for c in chars[int(digits[i])]:
                subset.append(c)
                backtrack(i + 1)
                subset.pop()
        
        backtrack(0)
        return res
