class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        l = r = 0
        maxlen = 0
        for r in range(len(s)):
            if s[r] in charMap and l <= charMap[s[r]]:
                l = charMap[s[r]] + 1
            charMap[s[r]] = r
            maxlen = max(maxlen, r-l+1)
        return maxlen