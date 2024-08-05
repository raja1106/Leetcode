class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        global_ans =0

        for row in range (m):
            for col in range(n):
                if matrix[row][col] == '1':
                    heights[col] += 1
                else:
                    heights[col] = 0
            local_ans = self.largestRectangleArea(heights)
            global_ans = max(global_ans,local_ans)

        return global_ans
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
