class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # immutable
        chars = set()
        # dynamic
        freq = dict()
        char_state = set()

        for c in t:
            chars.add(c)
            freq[c] = freq.get(c, 0) + 1
        
        left = 0
        right = 0
        found = False
        mi = s

        for c in s:
            right += 1

            if c in chars:
                freq[c] -= 1
                
                if freq[c] <= 0:
                    char_state.add(c)

            # shrink as far as we can
            continue_min = True
            while len(char_state) == len(chars) and continue_min:
                found = True
                
                if len(mi) > right - left:
                    mi = s[left:right]

                if s[left] in chars:
                    if freq[s[left]] >= 0:
                        continue_min = False
                        continue

                    freq[s[left]] += 1
                
                # shrink if s[left] is not in t, and we have enough
                left += 1
        
        return mi if found else ""
