class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1map = [0]*26
        s2map = [0]*26
        for i in range(len(s1)):
            s1map[ord(s1[i]) - ord('a')] += 1
            s2map[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1map[i] == s2map[i]:
                matches += 1
        l, r = 0, len(s1)
        while r < len(s2):
            if matches == 26:
                return True

            # handle right char
            i = ord(s2[r]) - ord('a')
            s2map[i] += 1
            if s2map[i] == s1map[i]:
                matches += 1
            if s2map[i] - 1 == s1map[i]:
                matches -= 1
            r += 1
            
            # handle left char
            i = ord(s2[l]) - ord('a')
            s2map[i] -= 1
            if s2map[i] == s1map[i]:
                matches += 1
            if s2map[i] + 1 == s1map[i]:
                matches -= 1
            l += 1
            
        return matches == 26

        