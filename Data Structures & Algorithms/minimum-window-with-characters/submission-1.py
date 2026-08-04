class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        scount, tcount = [0]*128, [0]*128
        for i in range(len(t)):
            tcount[ord(t[i]) - ord("a")] += 1
        result = ""
        minSubstringLen = float("inf")
        l = 0
        for r in range(len(s)):
            scount[ord(s[r]) - ord("a")] += 1
            while self.contains(scount, tcount):
                if r-l+1 < minSubstringLen:
                    result = s[l:r+1]
                    minSubstringLen = r-l+1
                scount[ord(s[l]) - ord("a")] -= 1
                l += 1
        return result

    def contains(self, scount, tcount):
        for i in range(128):
            if tcount[i] == 0:
                continue
            if tcount[i] > scount[i]:
                return False
        return True

    