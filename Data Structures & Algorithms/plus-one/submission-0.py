class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = 0
        digits.reverse()

        while carry:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0
            else:
                digits.append(carry)
                carry = 0
            i += 1

        digits.reverse()
        return digits