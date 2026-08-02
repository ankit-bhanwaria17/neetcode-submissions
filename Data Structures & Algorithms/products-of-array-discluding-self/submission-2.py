class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        leftProd = 1
        for i in range(len(nums)):
            result.append(leftProd)
            leftProd *= nums[i]
        rightProd = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] = rightProd * result[i]
            rightProd *= nums[i]
        return result