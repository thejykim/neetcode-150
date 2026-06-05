class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        candidates.sort()

        def backtrack(start: int, curr: int):
            if curr == target:
                res.append(subset[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i - 1] == candidates[i]:
                    continue
                
                new_curr = curr + candidates[i]
                if new_curr > target:
                    break
                
                subset.append(candidates[i])
                backtrack(i + 1, new_curr)
                subset.pop()
        
        backtrack(0, 0)
        return res