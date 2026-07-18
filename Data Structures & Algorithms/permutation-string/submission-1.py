class Solution:
    def areListEqual(self, arr1, arr2):
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Count = [0 for i in range(26)]
        s2Count = [0 for i in range(26)]
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        l, r = 0, len(s1)-1
        print(s1Count)
        while r < len(s2) and r-l+1 == len(s1):
            if self.areListEqual(s1Count, s2Count):
                return True
            s2Count[ord(s2[l]) - ord('a')] -= 1
            l += 1
            if r+1 < len(s2):
                r += 1
                s2Count[ord(s2[r]) - ord('a')] += 1
            
        return False