import random
import bisect

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
        # Use binary search to find the target zone
        index = bisect.bisect_left(self.prefix_sums, target)
        return index
# Test Case 1: Single Weight
solution = Solution([10])
print([solution.pickIndex() for _ in range(10)])  # Expected output: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Test Case 2: Uniform Weights
solution = Solution([5, 5, 5, 5])
print([solution.pickIndex() for _ in range(10)])  # Expected output: Indices 0-3 should be equally likely

# Test Case 3: Different Weights
solution = Solution([1, 2, 3, 4])
print([solution.pickIndex() for _ in range(10)])  # Expected output: Higher indices more likely due to higher weights

# Test Case 4: Large Weights
solution = Solution([1000000, 1, 1])
print([solution.pickIndex() for _ in range(10)])  # Expected output: 0 should be picked almost always

# Test Case 5: Sparse Weights
solution = Solution([0, 10, 0, 5])
print([solution.pickIndex() for _ in range(10)])  # Expected output: Only indices 1 and 3 should be picked

# Test Case 6: Non-consecutive Weights
solution = Solution([1, 10, 3, 8])
print([solution.pickIndex() for _ in range(10)])  # Expected output: Indices should reflect weight proportion

# Test Case 7: Increasing Weights
solution = Solution([1, 2, 3, 4, 5])
print([solution.pickIndex() for _ in range(10)])  # Expected output: Higher indices more likely

# Test Case 8: Decreasing Weights
solution = Solution([5, 4, 3, 2, 1])
print([solution.pickIndex() for _ in range(10)])  # Expected output: Lower indices more likely
