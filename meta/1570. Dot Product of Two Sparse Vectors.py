from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        # Store the non-zero elements with their indices as keys
        self.non_zero_elements = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.non_zero_elements[i] = nums[i]

    # Return the dot product of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        # Determine the smaller and larger vectors based on the number of non-zero elements
        if len(self.non_zero_elements) < len(vec.non_zero_elements):
            smaller_vector = self.non_zero_elements
            larger_vector = vec.non_zero_elements
        else:
            smaller_vector = vec.non_zero_elements
            larger_vector = self.non_zero_elements

        # Calculate the dot product by summing the product of the overlapping elements
        dot_product = 0
        for index, value in smaller_vector.items():
            if index in larger_vector:
                dot_product += value * larger_vector[index]

        return dot_product

# Example usage:
# nums1 = [1, 0, 0, 2, 3]
# nums2 = [0, 3, 0, 4, 0]
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
# print(ans)  # Output will be 8
