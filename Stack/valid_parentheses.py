class Solution:
    def isValid(self, s: str) -> bool:
        brackets_mapping = {'(':')', '[':']', '{':'}'}
        
        str_len = len(s)
        if str_len % 2 != 0:
            return False
        
        stack = []
        for c in s:
            if c in brackets_mapping.keys():
                stack.append(c)
            elif c in brackets_mapping.values():
                if len(stack) == 0 or brackets_mapping[stack[-1]] != c:
                    return False
                stack.pop() 

        return True if len(stack) == 0 else False
