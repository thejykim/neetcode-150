class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        def dfs(x: int, y: int, prev: int, s: set):
            if x < 0 or y < 0 or x >= len(heights) or y >= len(heights[0]):
                return

            if (x, y) in s:
                return
            
            height = heights[x][y]
            
            if height < prev:
                return

            s.add((x, y))

            dfs(x + 1, y, height, s)
            dfs(x - 1, y, height, s)
            dfs(x, y + 1, height, s)
            dfs(x, y - 1, height, s)
        
        for i in range(len(heights)):
            dfs(i, 0, 0, pacific)
            dfs(i, len(heights[0]) - 1, 0, atlantic)
        
        for i in range(len(heights[0])):
            dfs(0, i, 0, pacific)
            dfs(len(heights) - 1, i, 0, atlantic)
        
        return [[r, c] for r in range(len(heights)) for c in range(len(heights[0])) if (r, c) in pacific and (r, c) in atlantic]