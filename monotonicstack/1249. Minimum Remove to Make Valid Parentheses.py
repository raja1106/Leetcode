class Solution_Single_Pass:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = set()

        # Pass 1: Find indices of unmatched ')' and keep track of '(' in a stack
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    stack.pop()  # We have a matching '(' on top of stack
                else:
                    to_remove.add(i)  # No matching '(' => remove this index

        # Anything left in stack are unmatched '(' => remove them as well
        to_remove = to_remove.union(set(stack))

        # Build the resulting string
        result = []
        for i, ch in enumerate(s):
            if i not in to_remove:
                result.append(ch)

        return "".join(result)


class Solution_Two_Pass:
    def minRemoveToMakeValid(self, s: str) -> str:

        # First pass: Remove unmatched ')'
        open_count = 0
        st = []
        for ch in s:
            if ch == '(':
                open_count += 1
                st.append(ch)
            elif ch == ')':
                if open_count > 0:
                    open_count -= 1  # Valid match, decrement
                    st.append(ch)
            else:
                st.append(ch)

        # Second pass: Remove unmatched '('
        close_count = 0
        result = []
        for ch in reversed(st):
            if ch == ')':
                close_count += 1
                result.append(ch)
            elif ch == '(':
                if close_count > 0:
                    close_count -= 1  # Valid match, decrement
                    result.append(ch)
            else:
                result.append(ch)

        # Reconstruct valid string
        return ''.join(reversed(result))


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
















