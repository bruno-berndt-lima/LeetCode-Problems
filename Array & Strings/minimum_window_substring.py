class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        t_count, window = {}, {}
        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)

        l = 0
        result, result_len = [-1, -1], float('inf')
        current_chars, required_chars = 0, len(t_count)
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in t_count and t_count[s[r]] == window[s[r]]:
                current_chars += 1

            while current_chars == required_chars:
                if r - l + 1 < result_len:
                    result = [l, r]
                    result_len = r - l + 1

                window[s[l]] -= 1
                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    current_chars -= 1

                l += 1

        l, r = result

        return s[l : r + 1] if result_len != float('inf') else ""
