class Solution_Bruteforce:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height)):
            right_height = height[i]
            for j in range(i,-1,-1):
                left_height = height[j]
                container_area = (i-j) * min(right_height,left_height)
                max_area = max(max_area,container_area)
        return max_area


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the current container's area
            current_area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, current_area)

            # Move the pointer that points to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
