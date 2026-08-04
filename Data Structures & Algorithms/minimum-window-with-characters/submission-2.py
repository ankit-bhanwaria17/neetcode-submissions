class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        tcount = {}
        for char in t:
            tcount[char] = 1 + tcount.get(char, 0)
        have, need = 0, len(tcount)
        result = ""
        minValidSize = float("inf")
        l = 0
        window = {}
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in tcount and window[s[r]] == tcount[s[r]]:
                have += 1
            while have == need:
                if r-l+1 < minValidSize:
                    minValidSize = r-l+1
                    result = s[l:r+1]
                window[s[l]] -= 1
                if s[l] in tcount and window[s[l]] < tcount[s[l]]:
                    have -= 1
                l += 1
        return result