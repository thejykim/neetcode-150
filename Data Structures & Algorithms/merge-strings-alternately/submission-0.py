class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # similar to merging two sorted linked lists
        pointer = 0
        res = []

        while pointer < len(word1) and pointer < len(word2):
            res.append(word1[pointer])
            res.append(word2[pointer])
            pointer += 1
        
        if len(word1) > len(word2):
            res.append(word1[pointer:])
        else:
            res.append(word2[pointer:])
        
        return "".join(res)