class Solution:
    def backtrack(self, openP, closeP, ans, res, n):
        print(f"openP = {openP}, closeP = {closeP}, ans = {ans}")
        if openP > n or closeP > n:
            return
        if closeP > openP:
            return
        if openP + closeP == 2*n:
            res.append(ans)
            return
        self.backtrack(openP+1, closeP, ans + "(", res,  n)
        self.backtrack(openP,closeP + 1, ans + ")", res, n)
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        openP = 0
        closeP = 0
        self.backtrack(openP + 1, closeP, "(", res, n)
        self.backtrack(openP, closeP + 1, ")", res, n)
        return res