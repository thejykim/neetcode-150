class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[a].append(b)
        
        visited = set()
        visiting = set()

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

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True