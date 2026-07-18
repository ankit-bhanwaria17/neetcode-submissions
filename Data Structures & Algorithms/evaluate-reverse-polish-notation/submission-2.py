class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c in ("+", "-", "*", "/"):
                y = int(stack.pop())
                x = int(stack.pop())
                print(f"{x} {c} {y}")
                if c == "+":
                    stack.append(x+y)
                elif c == "-":
                    stack.append(x-y)
                elif c == "*":
                    stack.append(x*y)
                else:
                    res = x/y
                    if res < 0:
                        res = math.ceil(res)
                    else:
                        res = math.floor(res)
                    stack.append(res)
                print(f"stack: {stack}")
            else:
                stack.append(int(c))
        return stack.pop()
        