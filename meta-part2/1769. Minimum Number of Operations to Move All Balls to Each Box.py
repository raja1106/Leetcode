from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0] * n
        left_steps = [0] * n
        right_steps = [0] * n

        # Calculate steps needed from the left side
        ball_count = int(boxes[0])
        for i in range(1, n):
            left_steps[i] = left_steps[i - 1] + ball_count
            ball_count += int(boxes[i])

        # Calculate steps needed from the right side
        ball_count = int(boxes[-1])
        for i in range(n - 2, -1, -1):
            right_steps[i] = right_steps[i + 1] + ball_count
            ball_count += int(boxes[i])

        # Final result: sum of steps from left and right
        for i in range(n):
            result[i] = left_steps[i] + right_steps[i]

        return result
