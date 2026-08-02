class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            count = [0]*26
            for w in word:
                count[ord(w)-ord("a")] += 1
            group = tuple(count)
            if group not in hashmap:
                hashmap[group] = []
            hashmap[group].append(word)
        return list(hashmap.values())
