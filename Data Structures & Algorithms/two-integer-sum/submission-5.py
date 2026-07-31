class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # One pass HashMap solution
        hashMap = {} # key: nums[i] -----> value: i
        for i, n in enumerate(nums):
            if target - n in hashMap and i != hashMap[target-n]:
                return [hashMap[target-n], i]
            hashMap[n] = i
            
        return []