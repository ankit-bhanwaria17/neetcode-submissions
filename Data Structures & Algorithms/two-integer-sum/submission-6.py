class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        res = []
        for i, n in enumerate(nums):
            if target - n in hashMap:
                res = [hashMap[target - n], i]
                break
            hashMap[n] = i
        return res