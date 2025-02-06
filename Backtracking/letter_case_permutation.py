class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = [""]

        for c in s:
            temp = []
            if c.isalpha():
                for a in res:
                    temp.append(a + c.lower())
                    temp.append(a + c.upper())
            else:
                for a in res:
                    temp.append(a + c)
            print(temp)

            res = temp

        return res
