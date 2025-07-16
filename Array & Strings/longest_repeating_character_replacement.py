class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        longest = 0
        char_freq = [0] * 26

        while r < len(s):
            char_freq[ord(s[r]) - ord('A')] += 1

            if (r - l + 1) - max(char_freq) <= k:
                longest = max(longest, r - l + 1)
            else:
                char_freq[ord(s[l]) - ord('A')] -= 1
                l += 1

            r += 1

        return longest
