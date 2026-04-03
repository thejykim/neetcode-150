from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = deque()

        for s in tokens:
            if s in '+-*/':
                op1 = operands.pop()
                op2 = operands.pop()

                if s == '+':
                    operands.append(op2 + op1)
                elif s == '-':
                    operands.append(op2 - op1)
                elif s == '*':
                    operands.append(op2 * op1)
                elif s == '/':
                    operands.append(int(op2 / op1))
            else:
                operands.append(int(s))
        
        return operands.pop()