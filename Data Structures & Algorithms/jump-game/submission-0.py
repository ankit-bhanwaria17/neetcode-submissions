class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = {}
        def dfs(i):
            if i == len(nums)-1:
                return True
            if nums[i] == 0:
                return False
            if i in cache:
                return cache[i]
            cache[i] = False
            for j in range(1, nums[i]+1):
                if dfs(i+j):
                    cache[i] = True
                    break
            return cache[i]
        return dfs(0)
            
