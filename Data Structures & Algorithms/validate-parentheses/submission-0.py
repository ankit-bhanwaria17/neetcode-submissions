class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for p in s:
            if p in closeToOpen:
                if stack and stack[-1] == closeToOpen[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return len(stack) == 0