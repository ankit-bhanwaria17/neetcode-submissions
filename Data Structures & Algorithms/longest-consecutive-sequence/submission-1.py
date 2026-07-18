class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set()
        for n in nums:
            lookup.add(n)
        maxSeqLen = 0
        for n in nums:
            if n-1 in lookup:
                continue
            seqLen = 0
            while n in lookup:
                seqLen += 1
                n += 1
            maxSeqLen = max(maxSeqLen, seqLen)
        return maxSeqLen
