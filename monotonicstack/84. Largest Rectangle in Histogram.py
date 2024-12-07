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


class Solution_nearst_Smallest_element:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1] * n  # Nearest smaller element to the left
        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        right = [n] * n  # Nearest smaller element to the right
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        max_area = 0
        for i in range(n):
            max_area = max(max_area, heights[i] * (right[i] - left[i] - 1))

        return max_area
