class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sFreqMap, tFreqMap = {}, {}
        for i in range(0, len(s)):
            sFreqMap[s[i]] = sFreqMap.get(s[i], 0) + 1
            tFreqMap[t[i]] = tFreqMap.get(t[i], 0) + 1
        return sFreqMap == tFreqMap