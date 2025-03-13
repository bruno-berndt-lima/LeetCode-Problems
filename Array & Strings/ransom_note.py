class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_map = defaultdict(int)

        for c in magazine:
            char_map[c] += 1

        for c in ransomNote:
            char_map[c] -= 1

            if char_map[c] < 0:
                return False

        return True
