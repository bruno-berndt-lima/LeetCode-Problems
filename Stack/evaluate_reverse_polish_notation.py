class Solution:
    def evalRPN(self, tokens: List[str]) -> int:  
        def perform_operation(operator, a, b):
            if operator == '+':
                return b + a
            elif operator == '-':
                return b - a
            elif operator == '*':
                return b * a
            elif operator == '/':
                return int(b / a)
            
            return None

        operators = {'+', '-', '*', "/"}

        res = 0
        stack = []
        for t in tokens:
            if t in operators:
                a = int(stack.pop())
                b = int(stack.pop())
                res = perform_operation(t, a, b)
                stack.append(res)
            else:
                stack.append(t)

        return res
