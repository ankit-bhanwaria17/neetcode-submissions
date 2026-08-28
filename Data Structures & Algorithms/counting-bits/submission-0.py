class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n+1):
            count = 0
            while num:
                num = num & (num-1)
                count += 1
            res.append(count)
        return res