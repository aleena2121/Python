from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    preMap = {i:[] for i in range(numCourses)}

    for u, v in prerequisites:
        preMap[u].append(v)

    visited = set()

    def dfs(course):
        if course in visited:
            return False
        if preMap[course] == []:
            return True
        visited.add(course)
        for i in preMap[course]:
            if not dfs(i):
                return False
        visited.remove(course)
        preMap[course] = []
        return True

    for course in range(numCourses):
        if not dfs(course):
            return False
    return True

numCourses = 2
prerequisites = [[1,0]]
print(canFinish(numCourses, prerequisites))