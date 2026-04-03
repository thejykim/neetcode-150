class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        output = list()

        for item in strs:
            charMap = self.mapChars(item)
            key = tuple(charMap.items())

            if key in anagrams:
                output[anagrams[key]].append(item)
            else:
                anagrams[key] = len(output)
                output.append([item])
        
        return output

    def mapChars(self, string: str) -> Dict[str, int]:
        count = {c: 0 for c in 'abcdefghijklmnopqrstuvwxyz'}

        for c in string:
            count[c] += 1
        
        return count
