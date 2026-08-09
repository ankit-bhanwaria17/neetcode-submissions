class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        for c, r in prerequisites:
            preMap[c].append(r)
        cycle = set()
        processed = set()
        def dfs(c):
            if c in cycle:
                return False
            if c in processed:
                return True
            cycle.add(c)
            for i in preMap[c]:
                if not dfs(i):
                    return False
            cycle.remove(c)
            processed.add(c)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
