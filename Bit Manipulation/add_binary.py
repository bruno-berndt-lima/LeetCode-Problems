class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res_sum = ""
        carry_over = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry_over:
            if i >= 0:
                carry_over += int(a[i])
                i -= 1
            if j >= 0:
                carry_over += int(b[j])
                j -= 1

            res_sum += str(carry_over % 2)
            carry_over //= 2

        return res_sum[::-1]


