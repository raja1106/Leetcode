from typing import List


class Solution_May_2025:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        For each bar, calculate the width of the largest rectangle
        where this bar is the smallest height.

        - previous_smaller[i] = index of first bar to the left smaller than heights[i]
        - next_smaller[i] = index of first bar to the right smaller than heights[i]
        """
        n = len(heights)
        previous_smaller = [-1] * n
        next_smaller = [n] * n
        stack = []  # (height, index)

        # Find previous smaller elements for each bar
        for current_index in range(n):
            while stack and stack[-1][0] >= heights[current_index]:
                stack.pop()
            if stack:
                previous_smaller[current_index] = stack[-1][1]
            stack.append((heights[current_index], current_index))
        # Reset stack for next smaller
        stack.clear()
        # Find next smaller elements for each bar
        for current_index in range(n - 1, -1, -1):
            while stack and stack[-1][0] >= heights[current_index]:
                stack.pop()
            if stack:
                next_smaller[current_index] = stack[-1][1]
            stack.append((heights[current_index], current_index))

        max_area = 0
        for i in range(n):
            # span or width = (i-previous_smallest_idx[i])+(next_smallest_idx[i]-i)-1
            width = (next_smaller[i] - previous_smaller[i] - 1)
            area = width * heights[i]
            max_area = max(max_area, area)

        return max_area


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
