class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l, r = 0, 0
        maxSize = 0
        posDict = {}
        while r < len(s):
            if s[r] in posDict and posDict[s[r]] >= l:
                l = posDict[s[r]] + 1
            else:
                size = r - l + 1
                maxSize = max(maxSize , size)
            posDict[s[r]] = r
            r += 1
        return maxSize
