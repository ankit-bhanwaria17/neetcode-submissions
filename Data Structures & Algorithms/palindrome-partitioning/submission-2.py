class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def isPalindrom(word):
            l, r = 0, len(word)-1
            while l <= r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(ans, i, substring):
            if i == len(s):
                if isPalindrom(substring):
                    ans.append(substring)
                    result.append(ans[:])
                    ans.pop()
                return
            
            # Split

            if len(substring) > 0:
                if isPalindrom(substring):
                    ans.append(substring)
                    dfs(ans, i, "")
                    ans.pop()

            # Continue
            dfs(ans, i+1, substring + s[i])
        
        dfs([], 0, "")

        return result