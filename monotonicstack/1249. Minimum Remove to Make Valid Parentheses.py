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


class Solution_With_constant_Space_complexity:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)  # Convert to list for in-place modification

        # First pass: Remove unmatched ')'
        open_count = 0
        for i in range(len(s)):
            if s[i] == '(':
                open_count += 1
            elif s[i] == ')':
                if open_count == 0:  # Unmatched ')', remove it
                    s[i] = ''
                else:
                    open_count -= 1  # Valid match, decrement

        # Second pass: Remove unmatched '('
        close_count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')':
                close_count += 1
            elif s[i] == '(':
                if close_count == 0:  # Unmatched '(', remove it
                    s[i] = ''
                else:
                    close_count -= 1  # Valid match, decrement

        # Reconstruct valid string
        return ''.join(s)
















