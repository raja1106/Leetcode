class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        positive_index = len(nums)
        for i, val in enumerate(nums):
            if val >= 0:
                positive_index = i
                break
        negative_index = positive_index - 1
        result = []

        while negative_index >= 0 and positive_index < len(nums):
            if abs(nums[negative_index]) <= nums[positive_index]:
                result.append(nums[negative_index] ** 2)
                negative_index -= 1
            else:
                result.append(nums[positive_index] ** 2)
                positive_index += 1

        while negative_index >= 0:
            result.append(nums[negative_index] ** 2)
            negative_index -= 1

        while positive_index < len(nums):
            result.append(nums[positive_index] ** 2)
            positive_index += 1

        return result

    class Solution_Algo:
        def sortedSquares(self, nums: List[int]) -> List[int]:
            # Get the length of the input array
            length = len(nums)

            # Initialize a result array of the same length as the input array
            result = [0] * length

            # Initialize pointers for the start and end of the input array,
            # and a pointer for the position to insert into the result array
            start_pointer, end_pointer, result_pointer = 0, length - 1, length - 1

            # Loop through the array from both ends towards the middle
            while start_pointer <= end_pointer:
                # Square the values at both pointers
                start_square = nums[start_pointer] ** 2
                end_square = nums[end_pointer] ** 2

                # Compare the squared values and add the larger one to the end of the result array
                if start_square > end_square:
                    result[result_pointer] = start_square
                    start_pointer += 1
                else:
                    result[result_pointer] = end_square
                    end_pointer -= 1

                # Move the result pointer to the next position
                result_pointer -= 1

            # Return the sorted square array
            return result




