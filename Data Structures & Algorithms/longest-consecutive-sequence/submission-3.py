class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set()
        for n in nums:
            store.add(n)
        size = 1
        maxSize = 0
        for n in nums:
            if n-1 in store:
                continue
            while n+1 in store:
                size += 1
                n += 1                
            maxSize = max(maxSize, size)
            size = 1
        return maxSize