class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        seen_set = set()

        while n != 1 and n not in seen_set:           
            seen_set.add(n)
            
            n = str(n)
            result = 0
            for digit in n:
                result += int(digit) ** 2
            
            n = result         

        return True if n == 1 else False
