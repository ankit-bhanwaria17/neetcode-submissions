class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        leftProd = 1
        for n in nums:
            res.append(leftProd)
            leftProd *= n
        rightProd = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * rightProd
            rightProd *= nums[i]
        return res