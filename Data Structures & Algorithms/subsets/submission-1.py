class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        def dfs(i, subset):
            if i >= len(nums):
                self.result.append(subset[:])
                return
            subset.append(nums[i])
            dfs(i+1, subset)
            subset.pop()
            dfs(i+1, subset)

        dfs(0, [])
        return self.result