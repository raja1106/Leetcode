class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left_unmatched = 0  # Counts unmatched '('
        right_unmatched = 0  # Counts unmatched ')'

        for ch in s:
            if ch == '(':
                left_unmatched += 1
            elif ch == ')' and left_unmatched > 0:
                left_unmatched -= 1
            else:
                right_unmatched += 1

        return left_unmatched + right_unmatched

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        for ch in s:
            if ch == ')':
                if st and st[-1] == '(':
                    st.pop()
                else:
                    st.append(ch)
            else:
                st.append(ch)
        return len(st)
