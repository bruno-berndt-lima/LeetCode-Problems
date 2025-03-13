class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = [w for w in s.split(" ")]

        if len(pattern) != len(s):
            return False

        i = 0
        char_map = {}
        while i < len(pattern):
            if pattern[i] in char_map:
                if char_map[pattern[i]] != s[i]:
                    return False
            elif s[i] in char_map.values():
                return False

            char_map[pattern[i]] = s[i]
            i += 1

        return True
