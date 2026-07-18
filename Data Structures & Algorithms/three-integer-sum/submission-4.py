class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        i = 0
        while i < len(nums)-2:
            if i > 0 and nums[i-1] == nums[i]:
                i += 1
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                tripSum = nums[i] + nums[l] + nums[r]
                if tripSum > 0:
                    r -= 1
                elif tripSum < 0:
                    l += 1
                else:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
            i += 1
        return triplets