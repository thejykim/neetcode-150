class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, subset = [], []

        def backtrack(start: int):
            if start == len(s):
                res.append(subset[:])
                return
            
            for end in range(start, len(s)):
                curr = s[start:end + 1]

                if isPalindrome(curr):
                    subset.append(curr)
                    backtrack(end + 1)
                    subset.pop()
        
        def isPalindrome(s: str) -> bool:
            l, r = 0, len(s) - 1

            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            
            return True
        
        backtrack(0)
        return res
