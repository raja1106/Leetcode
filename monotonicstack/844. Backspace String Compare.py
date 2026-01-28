class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(x: str) -> str:
            st = []
            for ch in x:
                if ch == '#':
                    if st:
                        st.pop()
                else:
                    st.append(ch)
            return ''.join(st)

        return build(s) == build(t)


class Solution_With_Constant_space:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        skip_s = skip_t = 0

        while i >= 0 or j >= 0:
            # 1. Find next valid char in s
            while i >= 0:
                if s[i] == '#':
                    skip_s += 1
                    i -= 1
                elif skip_s > 0:
                    skip_s -= 1
                    i -= 1
                else:
                    break

            # 2. Find next valid char in t
            while j >= 0:
                if t[j] == '#':
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    j -= 1
                else:
                    break

            # 3. Compare the characters
            # Check if one pointer is exhausted and the other isn't
            if (i >= 0) != (j >= 0):
                return False

            # If both have characters, they must match
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False

            i -= 1
            j -= 1

        return True