class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.result = []
        nums.sort()
        def dfs(subset, start, total):
            if total == target:
                self.result.append(subset[:])
                return

            for i in range(start, len(nums)):
                if total + nums[i] > target:
                    return
                subset.append(nums[i])
                dfs(subset, i, total + nums[i])
                subset.pop()  
        
        dfs([], 0, 0)
        return self.result