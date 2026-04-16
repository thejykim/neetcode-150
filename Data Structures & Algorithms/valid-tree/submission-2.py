# a valid tree has no cycles, and connects all nodes.
# has n - 1 edges
from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        queue = deque()
        visited = set()

        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        queue.append((0, -1))

        while queue:
            node, prev = queue.popleft()

            if node in visited:
                return False
            
            visited.add(node)

            for dep in graph[node]:
                if dep != prev:
                    queue.append((dep, node))
                
        return len(visited) == n