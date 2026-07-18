class Solution:
    def hasDuplicate(self, nums: List[int]):
        count = set()
        for x in nums:
            if x in count:
                return True
            count.add(x)
        return False