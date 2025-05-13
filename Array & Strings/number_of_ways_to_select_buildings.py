class Solution:
    def numberOfWays(self, s: str) -> int:
        total_0 = s.count('0')
        total_1 = len(s) - total_0

        n_ways = 0
        count_0 = count_1 = 0

        for i in range(len(s)):
            if s[i] == '0':
                n_ways += count_1 * (total_1 - count_1)
                count_0 += 1
            else:
                n_ways += count_0 * (total_0 - count_0)
                count_1 += 1

        return n_ways
