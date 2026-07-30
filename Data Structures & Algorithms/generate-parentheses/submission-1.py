class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(openParen, closeParen, ans):
            print(f"open = {openParen}, close = {closeParen}, ans = {ans}, n = {n}")
            if openParen > n or closeParen > n:
                print("---------------------------------------------> Exit 1")
                return
            if openParen == n and closeParen == n:
                print("Added---------------------------------------------> Exit 2")
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