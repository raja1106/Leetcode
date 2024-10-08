from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 0:
            return 0
        # Arrays to store the left and right span
        left_span = [0] * n
        right_span = [0] * n

        # Stack for calculating left spans
        st = []
        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            left_span[i] = i - st[-1] if st else i + 1
            st.append(i)
        # Stack for calculating right spans
        st = []
        for i in range(n - 1, -1, -1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            right_span[i] = st[-1] - i if st else n - i
            st.append(i)
        # Calculate the maximum rectangle area
        max_area = 0
        for i in range(n):
            span = left_span[i] + right_span[i] - 1
            max_area = max(max_area, heights[i] * span)
        return max_area


class Solution_naive_approach:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # I am looking for next smaller element
        glaba_ans = -1
        length = len(heights)
        right_area = [0] * length
        st = []
        for i in range(length - 1, -1, -1):
            while st and st[-1][0] >= heights[i]:
                st.pop()
            if st:
                local_area = (st[-1][1] - i) * heights[i]
            else:
                local_area = heights[i] * (length - i)
            right_area[i] = local_area
            st.append((heights[i], i))
        # I am looking for previous smaller element

        left_area = [0] * length
        st = []
        for i in range(length):
            while st and st[-1][0] >= heights[i]:
                st.pop()
            if st:
                local_area = (i - st[-1][1]) * heights[i]
            else:
                local_area = heights[i] * (i + 1)
            left_area[i] = local_area
            st.append((heights[i], i))

        for i in range(length):
            total_area = left_area[i] + right_area[i] - heights[i]
            glaba_ans = max(glaba_ans, total_area)

        return glaba_ans

