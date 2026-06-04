from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''
        
        need = Counter(t)
        have = defaultdict(int)
        formed, required = 0, len(need)
        best, left = None, 0

        for right, c in enumerate(s):
            have[c] += 1
            if c in need and have[c] == need[c]:
                formed += 1

            while formed == required:
                window = s[left:right + 1]
                if not best or len(best) > len(window):
                    best = window
                
                left_c = s[left]
                have[left_c] -= 1
                if left_c in need and have[left_c] < need[left_c]:
                    formed -= 1
                
                left += 1
        
        return best if best else ''
