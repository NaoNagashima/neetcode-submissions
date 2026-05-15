class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {}

        for n in range(numCourses):
            preMap[n] = []

        for course, pre in prerequisites:
            preMap[course].append(pre)

        result = []
        visited = set()
        def dfs(course) -> bool:
            if course in visited:
                return False
            if preMap[course] == []:
                if course not in result:
                    result.append(course)
                return True
            visited.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            
            visited.remove(course)
            preMap[course] = []
            if course not in result:
                result.append(course)

            return True

        for n in range(numCourses):
            if n not in result:
                if not dfs(n):
                    return []
        
        return result