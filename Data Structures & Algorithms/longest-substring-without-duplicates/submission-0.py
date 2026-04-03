class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        right = 0
        freq = dict()

        for i in range(len(s)):
            while s[i] in freq:
                del freq[s[left]]
                left += 1

            # add
            freq[s[i]] = 1
            right += 1
            max_len = max(max_len, right - left)
        
        return max_len