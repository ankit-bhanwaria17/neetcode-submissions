class Solution:
    def reverse(self, x: int) -> int:
        def rec(n, rev):
            if n == 0:
                return rev
            rev = rev * 10 + n%10
            return rec(n // 10, rev)
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversedNum = rec(x, 0)
        reversedNum *= sign

        if reversedNum < -(1 << 31) or reversedNum > (1 << 31):
            return 0
        
        return reversedNum 