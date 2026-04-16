from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        queue = deque()

        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def bfs(node: int):
            queue.append(node)

            while queue:
                node = queue.popleft()

                if node in visited:
                    continue
                
                visited.add(node)
                
                for dep in graph[node]:
                    queue.append(dep)
        
        res = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                res += 1
        
        return res
