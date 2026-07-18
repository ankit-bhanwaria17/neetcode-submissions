class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l ,r = 0, 0
        maxLen = 0
        store = {}
        while r < len(s):
            if s[r] not in store or store[s[r]] < l:
                store[s[r]] = r
            else:
                l = store[s[r]] + 1
                store[s[r]] = r
            maxLen = max(maxLen, r - l + 1)
            r += 1    
        return maxLen