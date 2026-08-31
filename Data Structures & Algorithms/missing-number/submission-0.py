class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        hashset = set(nums)
        if 0 not in hashset:
            return 0
        if n not in hashset:
            return n
        for i in nums:
            if i != 0 and i-1 not in hashset:
                return i-1
        
            