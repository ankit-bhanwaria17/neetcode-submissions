class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Twop pass HashMap solution
        numsMap = {} # key: nums[i] -----> value: i
        for i in range(len(nums)):
            numsMap[nums[i]] = i

        for i in range(len(nums)):
            n = target - nums[i]
            if n in numsMap and i != numsMap[n]:
                return [i, numsMap[n]]
        return []