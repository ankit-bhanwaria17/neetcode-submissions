class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        a = 0
        res = []
        while a < len(nums)-2:
            if a != 0 and nums[a-1] == nums[a]:
                a += 1
                continue
            b, c = a+1, len(nums)-1
            while b < c:
                target = nums[a] + nums[b] + nums[c]
                if target == 0:
                    res.append([nums[a], nums[b], nums[c]])
                    b += 1
                    while nums[b-1] == nums[b] and b < c:
                        b += 1
                elif target > 0:
                    c -= 1
                else:
                    b += 1
            a += 1
        return res

                