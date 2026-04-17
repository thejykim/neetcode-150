from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append((v, t))
        
        heap = []
        heapq.heappush(heap, (0, k))
        visited = dict()

        while heap:
            cost, node = heapq.heappop(heap)

            if node in visited:
                continue
            
            visited[node] = cost

            for neighbor, n_cost in graph[node]:
                heapq.heappush(heap, (n_cost + cost, neighbor))
        
        return max(visited.values()) if len(visited) == n else -1