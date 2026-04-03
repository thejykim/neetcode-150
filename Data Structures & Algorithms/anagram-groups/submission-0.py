class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        output = list()

        for item in strs:
            key = "".join(sorted(item))

            if key in anagrams:
                output[anagrams[key]].append(item)
            else:
                anagrams[key] = len(output)
                output.append([item])
        
        return output
