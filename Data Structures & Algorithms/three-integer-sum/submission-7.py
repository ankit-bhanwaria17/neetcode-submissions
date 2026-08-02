class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i>0 and nums[i-1] == nums[i]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l, r = l+1, r-1
                    while l<r and nums[l-1] == nums[l]:
                        l += 1
        return result