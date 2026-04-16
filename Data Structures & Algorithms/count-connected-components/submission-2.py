class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()

        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node: int):
            if node in visited:
                return
            
            visited.add(node)
            
            for dep in graph[node]:
                dfs(dep)
            
        res = 0

        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        
        return res
