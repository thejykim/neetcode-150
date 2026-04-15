class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []

        def backtrack(start: int, curr: int):
            if curr == target:
                res.append(subset[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i - 1] == candidates[i]:
                    continue

                if curr + candidates[i] > target:
                    break
                
                subset.append(candidates[i])
                backtrack(i + 1, curr + candidates[i])
                subset.pop()
        
        backtrack(0, 0)
        return res
                