class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l ,r = 0, 0
        maxLen = 0
        positionMap = {}
        for r in range(len(s)):
            if s[r] in positionMap and positionMap[s[r]] >= l:
                l = positionMap[s[r]] + 1
            positionMap[s[r]] = r
            maxLen = max(maxLen, r - l + 1)
        return maxLen