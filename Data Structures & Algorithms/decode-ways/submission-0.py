class Solution:
    def numDecodings(self, s: str) -> int:
        hashmap = {len(s): 1}
        def dfs(i):
            if i in hashmap:
                return hashmap[i]
            if i > len(s) or s[i] == "0":
                return 0
            
            ways = dfs(i+1)
            if i+1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                ways += dfs(i+2)
            hashmap[i] = ways
            return ways

        return dfs(0)