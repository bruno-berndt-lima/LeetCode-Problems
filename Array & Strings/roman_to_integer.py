class Solution:
    def romanToInt(self, s: str) -> int:
        nums_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 0
        res = 0
        while i < len(s) - 1:
            if nums_map[s[i]] >= nums_map[s[i + 1]]:
                res += nums_map[s[i]]
            else:
                res -= nums_map[s[i]]
            i += 1

        res += nums_map[s[-1]]

        return res
