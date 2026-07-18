class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        res = []
        while i < len(nums)-2:
            if i != 0 and nums[i-1] == nums[i]:
                i += 1
                continue
            j, k = i+1, len(nums)-1
            while j < k:
                add = nums[i] + nums[j] + nums[k]
                if add == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
                    continue
                if add > 0:
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                else:
                    j += 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
            i += 1
        return res

                