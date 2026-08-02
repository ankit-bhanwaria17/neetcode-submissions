class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        for n in nums:
            hashset.add(n)
        maxlen = 0
        for n in nums:
            if n-1 in hashset:
                continue
            currlen = 1
            nextNum = n+1
            while nextNum in hashset:
                currlen += 1
                nextNum += 1
            maxlen = max(maxlen, currlen)
        return maxlen
