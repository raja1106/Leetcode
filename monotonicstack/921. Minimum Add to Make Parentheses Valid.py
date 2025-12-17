class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        needed_count = 0

        for ch in s:
            if ch == '(':
                st.append(ch)
            else:
                if st:
                    st.pop()
                else:
                    needed_count += 1

        return needed_count+len(st)


class Solution_Another_Approach:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        ans = 0
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