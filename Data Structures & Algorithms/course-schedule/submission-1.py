class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        for c, r in prerequisites:
            preMap[c].append(r)
        visitedSet = set()
        def dfs(c):
            if c in visitedSet:
                return False
            if preMap[c] == []:
                return True
            visitedSet.add(c)
            for i in preMap[c]:
                if not dfs(i):
                    return False
            visitedSet.remove(c)
            preMap[c] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
