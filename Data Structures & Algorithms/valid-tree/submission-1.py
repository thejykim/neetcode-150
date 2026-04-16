# a valid tree has no cycles, and connects all nodes.
# has n - 1 edges

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        graph = [[] for _ in range(n)]
        visited = set()

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node: int, prev: int) -> bool:
            if node in visited:
                return False
            
            visited.add(node)
            
            for dep in graph[node]:
                if dep != prev and not dfs(dep, node):
                    return False

            return True
        
        if not dfs(0, -1):
            return False
            
        return len(visited) == n