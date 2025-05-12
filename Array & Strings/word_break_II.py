class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words_set = set(wordDict)

        def helper(start):
            valid_substr = []

            if start == len(s):
                valid_substr.append("")
            
            for end in range(start + 1, len(s) + 1):
                prefix = s[start:end]
                if prefix in words_set:
                    suffixes = helper(end)
                    for suffix in suffixes:
                        valid_substr.append(prefix + ("" if suffix == "" else " ") + suffix)
            return valid_substr

        return helper(0)
