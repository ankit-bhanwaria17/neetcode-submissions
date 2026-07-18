class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        res = []
        for i in range(len(nums)):
            if target - nums[i] in pos:
                res = [pos[target-nums[i]], i]
                break
            else:
                pos[nums[i]] = i
        return res