class Solution:
    def validPalindrome(self, s: str) -> bool:
        # deleted = False
        # r a c e c a l r
        #   ^         ^

        deleted = False

        def isPalindrome(l, r):
            nonlocal deleted

            if l >= r:
                return True
            
            if not s[l].isalnum():
                return isPalindrome(l + 1, r)
            elif not s[r].isalnum():
                return isPalindrome(l, r - 1)
            
            if s[l] != s[r]:
                if deleted:
                    return False
                else:
                    deleted = True
                    return isPalindrome(l + 1, r) or isPalindrome(l, r - 1)
            
            return isPalindrome(l + 1, r - 1)

        return isPalindrome(0, len(s) - 1)