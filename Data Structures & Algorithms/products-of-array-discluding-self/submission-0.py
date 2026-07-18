class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod = 1
        for n in nums:
            res.append(prod)
            prod = prod * n
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = prod * res[i]
            prod = prod * nums[i]
        return res