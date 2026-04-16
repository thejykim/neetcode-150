class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visiting = set()
        visited = set()
        res = []

        graph = [[] for _ in range(numCourses)]
        
        for a, b in prerequisites:
            graph[a].append(b)
        
        def dfs(course: int) -> bool:
            if course in visited:
                return True
            if course in visiting:
                return False
            
            visiting.add(course)

            for dep in graph[course]:
                if not dfs(dep):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            res.append(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []

        return res