import random


class Solution:
    def __init__(self, w):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self):
        target = random.randint(1, self.total_sum)
        # Perform binary search manually to find the target zone
        low, high = 0, len(self.prefix_sums) - 1

        while low < high:
            mid = (low + high) // 2
            if self.prefix_sums[mid] < target:
                low = mid + 1
            else:
                high = mid

        return low


# Example usage:
w = [1, 3, 4, 2]
solution = Solution(w)
print(solution.pickIndex())
print(solution.pickIndex())
print(solution.pickIndex())
print(solution.pickIndex())
print(solution.pickIndex())
print(solution.pickIndex())
print(solution.pickIndex())
