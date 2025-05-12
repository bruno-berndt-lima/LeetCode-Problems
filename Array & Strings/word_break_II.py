class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words_set = set(wordDict)

        def backtrack(i):
            if i == len(s):
                result.append(" ".join(curr))

            for j in range(i, len(s)):
                word = s[i:j + 1]
                if word in words_set:
                    curr.append(word)
                    backtrack(j + 1)
                    curr.pop()
        
        curr = []
        result = []
        backtrack(0)
        
        return result
