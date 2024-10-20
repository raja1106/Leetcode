class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []
        open_count = 0
        for c in s:
            if c == ')' and open_count == 0:
                continue
            if c == '(':
                open_count += 1
            elif c == ')':
                open_count -= 1
            stack.append(c)

        closed_count = 0
        answer = []
        for c in reversed(stack):
            if c == '(' and closed_count == 0:
                continue
            if c == ')':
                closed_count += 1
            elif c == '(':
                closed_count -= 1
            answer.append(c)

        return ''.join(reversed(answer))















