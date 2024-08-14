class Solution:
    def findRLEArray(self, rle_encoded1: List[List[int]], rle_encoded2: List[List[int]]) -> List[List[int]]:
        expanded_array1 = []
        expanded_array2 = []

        # Expand the first RLE encoded array
        for value, frequency in rle_encoded1:
            expanded_array1.extend([value] * frequency)

        # Expand the second RLE encoded array
        for value, frequency in rle_encoded2:
            expanded_array2.extend([value] * frequency)

        # Multiply corresponding elements in the expanded arrays
        multiplied_array = [expanded_array1[i] * expanded_array2[i] for i in range(len(expanded_array1))]

        # Compress the multiplied array back into RLE format
        rle_result = []
        current_count = 1
        current_value = multiplied_array[0]

        for i in range(1, len(multiplied_array)):
            if multiplied_array[i] == multiplied_array[i - 1]:
                current_count += 1
            else:
                rle_result.append([current_value, current_count])
                current_value = multiplied_array[i]
                current_count = 1
            if i == len(multiplied_array) - 1:
                rle_result.append([current_value, current_count])

        return rle_result


class Solution1: # Below code to avoid Memory error
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        rle_result = []
        i, j = 0, 0
        while i < len(encoded1) and j < len(encoded2):
            value1, frequency1 = encoded1[i]
            value2, frequency2 = encoded2[j]

            # Find the minimum frequency between the two
            min_frequency = min(frequency1, frequency2)

            # Multiply the values and add to the result
            multiplied_value = value1 * value2
            if rle_result and rle_result[-1][0] == multiplied_value:
                rle_result[-1][1] += min_frequency
            else:
                rle_result.append([multiplied_value, min_frequency])

            # Reduce the frequencies in the original lists
            encoded1[i][1] -= min_frequency
            encoded2[j][1] -= min_frequency

            # Move to the next element if the frequency reaches zero
            if encoded1[i][1] == 0:
                i += 1
            if encoded2[j][1] == 0:
                j += 1

        return rle_result

