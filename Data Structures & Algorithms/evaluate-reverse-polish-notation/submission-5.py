class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ("+", "-", "*", "/"):
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                if t == "+":
                    stack.append(n1 + n2)
                if t == "-":
                    stack.append(n1 - n2)
                if t == "*":
                    stack.append(n1 * n2)
                if t == "/":
                    stack.append(int(n1/n2))
            else:
                stack.append(t)   
        return int(stack.pop())
