class Solution:
    def reverseBits(self, n: int) -> int:
        bits = [0]*32
        for i in range(32):
            bit = (n >> i) & 1
            if bit == 1:
                bits[i] = bit
        result = 0
        for b in bits:
            result = (result << 1) | b
        return result