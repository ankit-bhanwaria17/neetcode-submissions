class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {} 
        window = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        have = 0
        need = len(countT)
        res = [-1, -1]
        resLen = float("infinity")
        l, r = 0, 0
        while r < len(s):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in countT and countT[s[r]] == window[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < resLen:
                    res = [l , r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            r += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
