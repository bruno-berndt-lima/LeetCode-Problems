class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        char_set = set()
        slow = 0

        for fast in range(len(s)):
            while s[fast] in char_set:
                char_set.remove(s[slow])
                slow += 1

            char_set.add(s[fast])
            max_length = max(max_length, fast - slow + 1)

        return max_length
