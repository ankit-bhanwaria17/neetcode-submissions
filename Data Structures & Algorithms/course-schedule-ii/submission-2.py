class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for crs, preq in prerequisites:
            preMap[crs].append(preq)
        cycle = set()
        output = []
        processed = []

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
            processed.append(c)
            output.append(c)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output