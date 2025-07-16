class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        char_freq_s1 = [0] * 26
        char_freq_s2 = [0] * 26

        for i in range(n1):
            char_freq_s1[ord(s1[i]) - ord('a')] += 1
            char_freq_s2[ord(s2[i]) - ord('a')] += 1

        for i in range(n2 - n1):
            if char_freq_s1 == char_freq_s2:
                return True
            
            char_freq_s2[ord(s2[i]) - ord('a')] -= 1
            char_freq_s2[ord(s2[i + n1]) - ord('a')] += 1

        return char_freq_s1 == char_freq_s2
