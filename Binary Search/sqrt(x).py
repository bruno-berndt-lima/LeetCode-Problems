class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        sqrt = 0

        while l <= r:
            m = (r + l) // 2

            if m * m > x:
                r = m - 1
            elif m * m < x:
                l = m + 1
                sqrt = m
            else:
                return m

        return sqrt
