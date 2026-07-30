class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(openParen, closeParen, ans):
            if openParen == closeParen == n:
                result.append("".join(ans))
                return

            if openParen < n:
                ans.append("(")
                dfs(openParen + 1, closeParen, ans)
                ans.pop()

            if openParen > closeParen:
                ans.append(")")
                dfs(openParen, closeParen + 1, ans)
                ans.pop()
        
        dfs(0, 0, [])
        return result