class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len, n_len = len(haystack), len(needle)

        if h_len < n_len:
            return -1

        i = p_h = p_n = 0

        while p_h < h_len and p_n < n_len:
            if haystack[p_h] == needle[p_n]:
                p_h += 1
                p_n += 1
            else:
                p_h = i + 1
                p_n = 0
                i = p_h

            if p_n == n_len:
                return i

        return -1
