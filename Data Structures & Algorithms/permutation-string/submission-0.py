class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = dict()

        for c in s1:
            freq[c] = freq.get(c, 0) + 1
        
        left = 0
        right = 0

        for c in s2:
            right += 1
            freq[c] = freq.get(c, 0) - 1

            if (freq[c] == 0):
                del freq[c]
            
            if (len(freq) == 0):
                return True
            elif right - left < len(s1):
                continue
            
            left_c = s2[left]
            freq[left_c] = freq.get(left_c, 0) + 1

            if (freq[left_c] == 0):
                del freq[left_c]
            
            left += 1
            
        return False