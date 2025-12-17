class Solution_Best_Approach:
    def longestValidParentheses(self, s: str) -> int:
        max_count = 0
        st = []

        for i, ch in enumerate(s):
            # Case 1: opening bracket → push and move on
            if ch == '(':
                st.append((ch, i))
                continue

            # Case 2: closing bracket but no matching '(' → push boundary
            if not st or st[-1][0] != '(':
                st.append((ch, i))
                continue

            # Case 3: valid match
            st.pop()

            # compute length using last unmatched index (or start)
            last_index = st[-1][1] if st else -1
            max_count = max(max_count, i - last_index)

        return max_count


class Solution_2nd_Approach:
    def longestValidParentheses(self, s: str) -> int:

        i = 0
        max_count = 0
        st = []
        for i, ch in enumerate(s):
            if ch == ')':
                if st and st[-1][0] == '(':
                    st.pop()
                    if st:
                        max_count = max(max_count, i - st[-1][1])
                    else:
                        max_count = max(max_count, i + 1)
                else:
                    st.append((ch, i))
            else:
                st.append((ch, i))

        return max_count


class Solution_3rd_Approach:
    def longestValidParentheses(self, s: str) -> int:
        max_count = 0
        st = []

        for i, ch in enumerate(s):
            # Case 1: opening bracket → push and move on
            if ch == '(':
                st.append((ch, i))
                continue

            # Case 2: closing bracket but no matching '(' → push boundary
            if not st or st[-1][0] != '(':
                st.append((ch, i))
                continue

            # Case 3: valid match
            st.pop()

            # compute length using last unmatched index (or start)
            last_index = st[-1][1] if st else -1
            max_count = max(max_count, i - last_index)

        return max_count

