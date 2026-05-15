class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = {}

        for n in range(numCourses):
            prereqMap[n] = []

        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)

        visited = set()

        def dfs(course) -> bool:
            if course in visited:
                return False
            if prereqMap[course] == []:
                return True

            prereqList = prereqMap[course]
            visited.add(course)
            for prereq in prereqList:
                if not dfs(prereq):
                    return False
            prereqMap[course] = []
            visited.remove(course)
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return False
        
        return True