class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        merged_str = ""
        i = 0
        while i < n or i < m:
            if i < n:
                merged_str += word1[i]
            if i < m:
                merged_str += word2[i]
            i += 1

        return merged_str
