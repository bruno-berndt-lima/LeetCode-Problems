class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        reversed_num = 0
        is_negative = x < 0
        x = abs(x)

        while x != 0:
            last_digit = x % 10
            x //= 10

            # Check for 32-bit overflow before multiplying
            if reversed_num > (INT_MAX - last_digit) // 10:
                return 0

            reversed_num = reversed_num * 10 + last_digit

        return -reversed_num if is_negative else reversed_num
