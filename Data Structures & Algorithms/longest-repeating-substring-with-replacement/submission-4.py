class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ma = 0
        left = 0
        right = 0
        freq = dict()
        target_char = ('a', 0)

        for c in s:
            right += 1
            freq[c] = freq.get(c, 0) + 1
            
            if target_char[1] < freq[c]:
                target_char = (c, freq[c])
            
            if right - left - target_char[1] > k:
                freq[s[left]] -= 1
                left += 1
                continue

            ma = max(ma, right - left)
        
        return ma
        

        
