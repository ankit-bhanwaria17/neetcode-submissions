class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []

        def dfs(i, ans):
            if i >= len(digits):
                if ans:
                    result.append("".join(ans))
                return
            
            for letter in keypad[digits[i]]:
                ans.append(letter)
                dfs(i+1, ans)
                ans.pop()
        
        dfs(0, [])
        return result
