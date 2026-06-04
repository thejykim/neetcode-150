from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for c in s:
            if c in '({[':
                stack.appendleft(c)
            else:
                if not stack:
                    return False
                
                if c == ')':
                    if stack.popleft() != '(':
                        return False
                elif c == '}':
                    if stack.popleft() != '{':
                        return False
                else:
                    if stack.popleft() != '[':
                        return False
        
        return not stack