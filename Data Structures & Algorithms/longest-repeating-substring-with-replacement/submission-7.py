class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqmap = {}
        l, r = 0, 0
        maxfreq = 0
        maxsize = 0
        while r < len(s):
            freqmap[s[r]] = 1 + freqmap.get(s[r], 0)
            maxfreq = max(maxfreq, freqmap[s[r]])
            size = r-l+1
            if size - maxfreq <= k:
                maxsize = max(maxsize, size)
            else:
                freqmap[s[l]] -= 1
                l += 1
            r += 1
        return maxsize