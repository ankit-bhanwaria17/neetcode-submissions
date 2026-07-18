class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in ["(", "{", "["]:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if (
                    (top == "(" and s[i] != ")") 
                    or (top == "{" and s[i] != "}") 
                    or (top == "[" and s[i] != "]")
                ):
                    return False
        return len(stack) == 0