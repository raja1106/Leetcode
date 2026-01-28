from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        st = []
        for log in logs:
            if log == './':
                continue
            if log == '../':
                if st:
                    st.pop()
            else:
                st.append(log)

        return len(st)


class Solution_Using_Constant_Space:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0

        for log in logs:
            if log == '../':
                # Can't go above the main folder, so stay at 0
                if depth > 0:
                    depth -= 1
            elif log != './':
                # It's a folder name like "d1/", go deeper
                depth += 1

        return depth