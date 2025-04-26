from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        extra_open = extra_close = 0

        count = 0
        for ch in s:
            if ch == '(':
                count += 1
            elif ch == ')':
                if count > 0:
                    count -= 1
                else:
                    extra_close += 1
        extra_open = count
        result_set = set()

        def is_valid(expr):
            count = 0
            for ch in expr:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        def helper(i, open_rem, close_rem, slate):
            if i == len(s):
                if open_rem == 0 and close_rem == 0:
                    candidate = ''.join(slate)
                    if is_valid(candidate):
                        result_set.add(candidate)
                return

            ch = s[i]

            if ch == '(':
                # Skip this '(' if open_rem > 0
                if open_rem > 0:
                    helper(i + 1, open_rem - 1, close_rem, slate)
                # Include this '('
                slate.append(ch)
                helper(i + 1, open_rem, close_rem, slate)
                slate.pop()

            elif ch == ')':
                # Skip this ')' if close_rem > 0
                if close_rem > 0:
                    helper(i + 1, open_rem, close_rem - 1, slate)
                # Include this ')'
                slate.append(ch)
                helper(i + 1, open_rem, close_rem, slate)
                slate.pop()

            else:
                # Just include non-parenthesis characters
                slate.append(ch)
                helper(i + 1, open_rem, close_rem, slate)
                slate.pop()

        helper(0, extra_open, extra_close, [])
        return list(result_set)
