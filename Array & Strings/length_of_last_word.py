class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        right = len(s) - 1

        while s[right] == ' ' and right >= 0:
            right -= 1

        left = right

        while s[left] != ' ' and left >= 0:
            left -= 1

        return right - left
