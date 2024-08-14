from typing import List
class Solution:
    def counting_sort(self,arr: List[int]):

        # Finds max and min elements
        max_element = max(arr)
        min_element = min(arr)

        # Stores the frequency(count) of each element of the given array
        frequency = [0] * (max_element - min_element + 1)

        # Finds the frequency of each element of the given array
        for i in range(len(arr)):
            frequency[arr[i] - min_element] += 1

        # Finds and store the cumulative sum
        for i in range(1, len(frequency)):
            frequency[i] += frequency[i - 1]

        # This will be the output array in the sorted order
        sorted_array = [None] * len(arr)

        # Finds the index of each element of the given array(the value of the given array
        # will be the corresponding index at the sorted_array) in the sorted array
        # and subtract the element by 1 and places it(the value) at the corresponding index at the sorted_array
        for i in range(len(arr) - 1, -1, -1):
            sorted_array[frequency[arr[i] - min_element] - 1] = arr[i]
            frequency[arr[i] - min_element] -= 1

        # Returns the sorted array
        return sorted_array

    class Solution_Using_Counting_Sort_LC_1122:
        def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
            # Find the maximum value in arr1 to determine the size of the count array
            max_val = max(arr1)

            # Initialize a count array to store frequencies
            count = [0] * (max_val + 1)

            # Populate the count array with frequencies of each number in arr1
            for num in arr1:
                count[num] += 1

            # List to store the result
            result = []

            # Add elements to result according to the order in arr2
            for num in arr2:
                result.extend([num] * count[num])
                count[num] = 0  # Set to 0 as those elements are already used

            # Add the remaining elements not in arr2, in sorted order
            for num in range(max_val + 1):
                if count[num] > 0:
                    result.extend([num] * count[num])

            return result

    # Using counting sort to sort the elements in the basis of significant places
    def countingSort(array, place):
        size = len(array)
        output = [0] * size
        count = [0] * 10

        # Calculate count of elements
        for i in range(0, size):
            index = array[i] // place
            count[index % 10] += 1

        # Calculate cumulative count
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Place the elements in sorted order
        i = size - 1
        while i >= 0:
            index = array[i] // place
            output[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(0, size):
            array[i] = output[i]

    # Main function to implement radix sort
    def radixSort(array):
        # Get maximum element
        max_element = max(array)

        # Apply counting sort to sort elements based on place value.
        place = 1
        while max_element // place > 0:
            countingSort(array, place)
            place *= 10

    data = [121, 432, 564, 23, 1, 45, 788]
    radixSort(data)
    print(data)


obj = Solution()
print(obj.counting_sort([4,2,5,1,7,3]))