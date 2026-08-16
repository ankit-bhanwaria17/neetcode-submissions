class Solution:
    def jump(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i):
            if i >= len(nums)-1:
                return 0
            if i in cache:
                return cache[i]
            path = float("inf")
            for j in range(1, nums[i]+1):
                path = min(path, dfs(i+j))
            cache[i] = 1 + path
            return cache[i]
        return dfs(0)