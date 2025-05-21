class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        max_area = 0
        n = len(nums)
        if n == 0:
            return 0
        # Arrays to store the left and right span
        left_span = [0] * n
        right_span = [0] * n

        # Stack for calculating left spans
        st = []
        for i in range(n):
            while st and nums[st[-1]] >= nums[i]:
                st.pop()
            left_span[i] = i - st[-1] if st else i + 1
            st.append(i)
        # Stack for calculating right spans
        st = []
        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] >= nums[i]:
                st.pop()
            right_span[i] = st[-1] - i if st else n - i
            st.append(i)
        # Calculate the maximum rectangle area
        for i in range(n):
            if i-left_span[i]+1 <= k <= i+right_span[i]-1:
                span = left_span[i] + right_span[i] - 1
                max_area = max(max_area, nums[i] * span)
        return max_area


class Solution_Another_Monotonic_Approach:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = [-1] * n  # Nearest smaller element to the left
        stack = []

        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        right = [n] * n  # Nearest smaller element to the right
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        max_score = 0
        for i in range(n):
            # Ensure the subarray between left[i] and right[i] includes index `k`
            if left[i] < k < right[i]:
                max_score = max(max_score, nums[i] * (right[i] - left[i] - 1))

        return max_score


class Solution_Greedy_Approach: #O(n)
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = k, k  # Initialize the sliding window
        max_score = nums[k]
        current_min = nums[k]

        # Expand the window while either side can grow
        while left > 0 or right < n - 1:
            # Choose the side to expand based on which value is greater
            expand_right = (right < n - 1 and (left == 0 or nums[right + 1] >= nums[left - 1]))
            #a and (b or c) = b or (a and c)
            #if (left == 0) or (right < n - 1 and nums[right + 1] >= nums[left - 1]):

            if expand_right:
                right += 1
                current_min = min(current_min, nums[right])
            else:
                left -= 1
                current_min = min(current_min, nums[left])

            # Calculate the current score and update the maximum score
            max_score = max(max_score, current_min * (right - left + 1))

        return max_score
