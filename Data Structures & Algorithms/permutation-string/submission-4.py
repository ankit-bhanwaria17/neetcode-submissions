class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1count = [0]*26
        s2count = [0]*26
        for s in s1:
            s1count[ord(s)-ord("a")] += 1
        l = 0
        r = 0
        while r < len(s1):
            s2count[ord(s2[r]) - ord("a")] += 1
            r += 1
        while r < len(s2):
            if self.isAnagram(s1count, s2count):
                return True
            else:
                s2count[ord(s2[r]) - ord("a")] += 1
                s2count[ord(s2[l]) - ord("a")] -= 1
                l += 1
                r += 1
        return self.isAnagram(s1count, s2count)
            
    def isAnagram(self, s1count, s2count):
        print(f"{s2count}")
        for i in range(len(s1count)):
            if s1count[i] != s2count[i]:
                return False
        return True
