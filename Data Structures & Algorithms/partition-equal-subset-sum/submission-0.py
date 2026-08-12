class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total/2
        def dfs(i, currSum):
            if currSum > target or i == len(nums):
                return False
            if currSum == target:
                return True
            return dfs(i+1, currSum + nums[i]) or dfs(i+1, currSum)
        return dfs(0, 0)