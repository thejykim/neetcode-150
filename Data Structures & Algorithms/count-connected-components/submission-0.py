class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))

        def find(a: int) -> int:
            while a != parent[a]:
                a = parent[a]
            return a
        
        def union(a: int, b: int):
            parent[find(a)] = find(b)
        
        for a, b in edges:
            union(a, b)

        return len(set(find(i) for i in range(n)))
