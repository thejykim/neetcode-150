class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))

        def find(a: int) -> int:
            while a != parent[a]:
                a = parent[a]
            return a
        
        def union(a: int, b: int):
            parent[find(a)] = find(b)
        
        for a, b in edges:
            if find(a) == find(b):
                return [a, b]
            else:
                union(a, b)
        
        return [0, 0]