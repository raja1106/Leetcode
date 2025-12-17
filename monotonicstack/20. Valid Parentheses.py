class Solution_Latest:
    def isValid(self, s: str) -> bool:
        """
        {}[
        last inserted
        """
        st = []

        opened = {'[', '{', '('}
        closed_map = {']': '[', '}': '{', ')': '('}

        for ch in s:
            if ch in closed_map:
                if st and st[-1] == closed_map[ch]:
                    st.pop()
                else:
                    return False
            else:
                st.append(ch)

        return False if st else True


class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map.values():  # Opening brackets
                stack.append(char)
            elif char in bracket_map:  # Closing brackets
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
            else:
                return False  # Invalid characters

        return not stack

    def isValid_mine(self, s: str) -> bool:
        st = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in bracket_map.values():
                st.append(c)
            elif c in bracket_map:
                if not st or st[-1] != bracket_map[c]:
                    return False
                st.pop()
            else:
                return False  # in case there are other characters

        return not st
