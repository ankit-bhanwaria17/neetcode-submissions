class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        cache = [0]*(len(nums))
        cache[0] = nums[0]
        cache[1] = max(nums[0], nums[1])
        # 1st house to 2nd last
        for i in range(2, len(nums)-1):
            cache[i] = max(
                nums[i] + cache[i-2],
                cache[i-1]
            )
        profit = cache[len(nums)-2]
        cache = [0]*(len(nums))
        cache[1] = nums[1]
        cache[2] = max(nums[1], nums[2])
        # 2nd to last house
        for i in range(3, len(nums)):
            cache[i] = max(
                nums[i] + cache[i-2],
                cache[i-1]
            )
        profit = max(profit, cache[len(nums)-1])
        return profit
        