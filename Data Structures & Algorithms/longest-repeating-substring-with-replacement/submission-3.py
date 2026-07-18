class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def maxFreqLetter(freqMap):
            res = 0
            for i in range(26):
                res = max(res, freqMap[i])
            return res

        freqMap = [0]*26
        l = 0
        result = 0
        for r in range(len(s)):
            freqMap[ord(s[r]) - ord('A')] += 1
            if (r - l + 1) - maxFreqLetter(freqMap) <= k:
                result = max(result, r - l + 1)
            else:
                freqMap[ord(s[l]) - ord('A')] -= 1
                l += 1
        return result

        