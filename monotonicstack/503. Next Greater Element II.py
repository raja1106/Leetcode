from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        st = []
        for i in range(len(nums) - 1, -1, -1):
            while st and st[-1] <= nums[i]:
                st.pop()
            st.append(nums[i])
        for i in range(len(nums) - 1, -1, -1):
            while st and st[-1] <= nums[i]:
                st.pop()
            if st:
                result[i] = st[-1]
            st.append(nums[i])
        return result


nums = [4, 1, 2, 3, 5] #4,1, 2, 3, 5,4, 1, 2, 3,5
print(Solution().nextGreaterElements(nums))
# Expected output: [5, 2, 3, 5, -1]
# Explanation: The next greater element for 4 is 5, for 1 is 2, and so on. The last element (5) has no greater element.

def run_test_cases():
    # Test Case 1: Distinct Elements (Increasing Order)
    nums = [1, 2, 3, 4, 5]
    expected_output = [2, 3, 4, 5, -1]
    print(f"Test Case 1: Input: {nums}, Expected Output: {expected_output}, Actual Output: {Solution().nextGreaterElements(nums)}")

    # Test Case 2: Distinct Elements (Decreasing Order)
    nums = [5, 4, 3, 2, 1]
    expected_output = [-1, 5, 5, 5, 5]
    print(f"Test Case 2: Input: {nums}, Expected Output: {expected_output}, Actual Output: {Solution().nextGreaterElements(nums)}")

    # Test Case 3: Repeated Elements
    nums = [2, 2, 2, 2]
    expected_output = [-1, -1, -1, -1]
    print(f"Test Case 3: Input: {nums}, Expected Output: {expected_output}, Actual Output: {Solution().nextGreaterElements(nums)}")

    # Test Case 4: Negative and Positive Elements
    nums = [-2, -1, 0, 1, 2]
    expected_output = [-1, 0, 1, 2, -1]
    print(f"Test Case 4: Input: {nums}, Expected Output: {expected_output}, Actual Output: {Solution().nextGreaterElements(nums)}")

    # Test Case 5: Single Element
    nums = [10]
    expected_output = [-1]
    print(f"Test Case 5: Input: {nums}, Expected Output: {expected_output}, Actual Output: {Solution().nextGreaterElements(nums)}")

    # Test Case 6: Alternating High and Low Values
    nums = [1, 10, 1, 10, 1]
    expected_output = [10, -1, 10, -1, 10]
    print(f"Test Case 6: Input: {nums}, Expected Output: {expected_output}, Actual Output: {Solution().nextGreaterElements(nums)}")

    # Test Case 7: All Elements the Same
    nums = [7, 7, 7, 7, 7]
    expected_output = [-1, -1, -1, -1, -1]
    print(f"Test Case 7: Input: {nums}, Expected Output: {expected_output}, Actual Output: {Solution().nextGreaterElements(nums)}")

    # Test Case 8: Non-Contiguous Array
    nums = [1, 5, 3, 6, 8, 4]
    expected_output = [5, 6, 6, 8, -1, 5]
    print(f"Test Case 8: Input: {nums}, Expected Output: {expected_output}, Actual Output: {Solution().nextGreaterElements(nums)}")

    # Test Case 9: Alternating Peak and Valley
    nums = [4, 1, 2, 3, 5]
    expected_output = [5, 2, 3, 5, -1]
    print(f"Test Case 9: Input: {nums}, Expected Output: {expected_output}, Actual Output: {Solution().nextGreaterElements(nums)}")

    # Test Case 10: Edge Case - Empty Array
    nums = []
    expected_output = []
    print(f"Test Case 10: Input: {nums}, Expected Output: {expected_output}, Actual Output: {Solution().nextGreaterElements(nums)}")

    # Test Case 11: Large Array Size
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected_output = [2, 3, 4, 5, 6, 7, 8, 9, 10, -1]
    print(f"Test Case 11: Input: {nums}, Expected Output: {expected_output}, Actual Output: {Solution().nextGreaterElements(nums)}")

# Running all test cases
run_test_cases()
