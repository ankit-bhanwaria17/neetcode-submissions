class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l, r = 0, 0
        maxSize = 0
        posDict = {}
        for r in range(len(s)):
            if s[r] in posDict and posDict[s[r]] >= l:
                l = posDict[s[r]] + 1
            maxSize = max(maxSize , r - l + 1)
            posDict[s[r]] = r
        return maxSize
