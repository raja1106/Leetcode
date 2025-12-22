from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        answer = []

        for i in range(len(temperatures) - 1, -1, -1):

            while st and st[-1][0] <= temperatures[i]:
                st.pop()

            if st:
                answer.append(st[-1][1] - i)
            else:
                answer.append(0)
            st.append((temperatures[i], i))

        answer.reverse()
        return answer
