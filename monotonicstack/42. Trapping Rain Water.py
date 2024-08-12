from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        # Fill left_max array
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        # Fill right_max array
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        # Calculate the total trapped water
        trapped_water = 0
        for i in range(n):
            trapped_water += min(left_max[i], right_max[i]) - height[i]

        return trapped_water

    from typing import List

class Solution_Using_Monotoic_Stack:
    def trap(self, height: List[int]) -> int:
        stack = []
        trapped_water = 0
        current = 0

        while current < len(height):
            # While stack is not empty and current height is greater than height at top index of stack
            while stack and height[current] > height[stack[-1]]:
                top = stack.pop()

                if not stack:
                    break

                distance = current - stack[-1] - 1
                bounded_height = min(height[current], height[stack[-1]]) - height[top]
                trapped_water += distance * bounded_height

            stack.append(current)
            current += 1

        return trapped_water


obj = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
height1 = [4,2,0,3,2,5]

print(obj.trap(height))

