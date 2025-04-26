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
import bisect


class SparseVector_Using_Binary_Search:
    def __init__(self, nums):
        """
        Initialize the sparse vector by storing only non-zero elements.
        Each element is stored as a tuple (index, value).
        """
        # Store only non-zero entries; the resulting list is sorted by index.
        self.non_zero = [(i, num) for i, num in enumerate(nums) if num != 0]

    def dotProduct(self, vec: 'SparseVector') -> int:
        """
        Compute the dot product of two sparse vectors using binary search.
        We iterate over the vector with fewer non-zero entries and for each
        entry, binary search for the same index in the other vector.
        """
        # Choose the sparse vector with fewer non-zero elements to iterate over.
        if len(self.non_zero) > len(vec.non_zero):
            return vec.dotProduct(self)

        result = 0
        # Extract the indices from the other vector for binary search.
        other_indices = [i for i, val in vec.non_zero]

        for i, val in self.non_zero:
            # Find the position where index i would be inserted in other_indices.
            pos = bisect.bisect_left(other_indices, i)
            # If the index is found in the other vector, multiply and add.
            if pos < len(other_indices) and other_indices[pos] == i:
                result += val * vec.non_zero[pos][1]

        return result

class SparseVector_TwoPointers:
    def __init__(self, nums):
        # Store (index, value) pairs, sorted by index
        self.non_zero = [(i, num) for i, num in enumerate(nums) if num != 0]

    def dotProduct(self, vec: 'SparseVector_TwoPointers') -> int:
        result = 0
        p1 = p2 = 0
        list1, list2 = self.non_zero, vec.non_zero

        while p1 < len(list1) and p2 < len(list2):
            index1, value1 = list1[p1]
            index2, value2 = list2[p2]

            if index1 == index2:
                result += value1 * value2
                p1 += 1
                p2 += 1
            elif index1 < index2:
                p1 += 1
            else:
                p2 += 1

        return result


import heapq


class SparseVector_HeapMerge:
    def __init__(self, nums):
        self.non_zero = [(i, num) for i, num in enumerate(nums) if num != 0]

    def dotProduct(self, vec: 'SparseVector_HeapMerge') -> int:
        result = 0
        heap = []

        # Initialize heap with first element from both lists
        if self.non_zero:
            heapq.heappush(heap, (self.non_zero[0][0], 0, 'self'))
        if vec.non_zero:
            heapq.heappush(heap, (vec.non_zero[0][0], 0, 'vec'))

        while heap:
            current_index, idx, owner = heapq.heappop(heap)

            # Advance the pointer of the current owner
            if owner == 'self':
                list_self = self.non_zero
                if idx + 1 < len(list_self):
                    heapq.heappush(heap, (list_self[idx + 1][0], idx + 1, 'self'))
                # Check if next item is from vec and has same index
                if heap and heap[0][0] == current_index and heap[0][2] == 'vec':
                    _, idx2, _ = heapq.heappop(heap)
                    result += list_self[idx][1] * vec.non_zero[idx2][1]
            else:
                list_vec = vec.non_zero
                if idx + 1 < len(list_vec):
                    heapq.heappush(heap, (list_vec[idx + 1][0], idx + 1, 'vec'))
                # Check if next item is from self and has same index
                if heap and heap[0][0] == current_index and heap[0][2] == 'self':
                    _, idx2, _ = heapq.heappop(heap)
                    result += vec.non_zero[idx][1] * self.non_zero[idx2][1]

        return result


# Example usage:
if __name__ == "__main__":
    # Consider two vectors:
    v1 = SparseVector([1, 0, 0, 2, 3])
    v2 = SparseVector([0, 3, 0, 4, 0])

    # The dot product is (1*0) + (2*4) + (3*0) = 8.
    print("Dot product:", v1.dotProduct(v2))  # Output should be 8
