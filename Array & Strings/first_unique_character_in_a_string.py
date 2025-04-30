class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_freq = [0] * 26

        for c in s:
            char_freq[ord(c) - ord('a')] += 1

        for index, c in enumerate(s):
            if char_freq[ord(c) - ord('a')] == 1:
                return index

        return -1
