class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []

        count = 0

        for c in s:
            if c == ')' and count == 0:
                continue
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            stack.append(c)

        count = 0
        answer = []
        for c in reversed(stack):
            if c == '(' and count == 0:
                continue
            if c == ')':
                count += 1
            elif c == '(':
                count -= 1
            answer.append(c)

        return ''.join(reversed(answer))















