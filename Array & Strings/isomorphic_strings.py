class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = {}

        i = 0
        while i < len(s):
            if s[i] in char_map:
                if char_map[s[i]] != t[i]:
                    return False
            elif t[i] in char_map.values():
                return False

            char_map[s[i]] = t[i]
            i += 1
        
        return True
