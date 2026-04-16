# a valid tree has no cycles, and connects all nodes.
# has n - 1 edges

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        parent = [i for i in range(n)]

        def find(a: int):
            while a != parent[a]:
                parent[a] = parent[parent[a]]
                a = parent[a]

            return a
        
        def union(a: int, b: int):
            parent[find(a)] = find(b)
        
        for a, b in edges:
            if find(a) == find(b):
                return False
            
            union(a, b)
        
        return True