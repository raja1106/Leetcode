class Solution_Using_Array:
    def maximumSwap(self, num: int) -> int:
        # Convert the number to a list of its digits.
        # Time: O(n), where n is the number of digits.
        digits = list(str(num))

        # Initialize a list to store the last occurrence of each digit (0-9).
        # Time: O(1) since the list size is constant (10).
        last_occurrence = [-1] * 10

        # Iterate over the digits to record the last index of each digit.
        # Time: O(n) iterations, each O(1) operation.
        for index, digit in enumerate(digits):
            last_occurrence[int(digit)] = index

        # Iterate over each digit to determine if a beneficial swap can be made.
        # Outer loop: O(n) iterations.
        for i, digit in enumerate(digits):
            # Inner loop: checks digits from 9 down to int(digit)+1.
            # This loop has at most 10 iterations (constant time, O(1)).
            for candidate in range(9, int(digit), -1):
                # Check if a higher candidate digit appears later in the number.
                # Time: O(1) per check.
                if last_occurrence[candidate] > i:
                    # Swap the current digit with the candidate digit.
                    # Time: O(1)
                    digits[i], digits[last_occurrence[candidate]] = digits[last_occurrence[candidate]], digits[i]
                    # Join the list back into a string and convert to int.
                    # Time: O(n) in the worst case.
                    return int(''.join(digits))

        # If no swap can improve the number, return the original number.
        # Time: O(1)
        return num


class Solution_Using_Map:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        #create a dictionary last that maps each digit to its last occurrence index in the number.
        digits_indices = {int(digit): i for i, digit in enumerate(digits)}

        for i, digit in enumerate(digits):
            for d in range(9, int(digit), -1):
                if digits_indices.get(d, -1) > i:
                    digits[i], digits[digits_indices[d]] = digits[digits_indices[d]], digits[i]
                    return int(''.join(digits))

        return num


class Solution_Bruteforce:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        count = 0
        for i, ch in enumerate(num_str):
            current_num = int(ch)
            max_num = current_num
            max_index = i
            for j in range(i + 1, len(num_str)):
                if int(num_str[j]) >= max_num:
                    max_num = int(num_str[j])
                    max_index = j
            if max_index != i and num_str[max_index] != num_str[i]:
                count += 1
                num_str[i], num_str[max_index] = num_str[max_index], num_str[i]
                break
        return int(''.join(num_str))


# Example usage:
solution = Solution()
print(solution.maximumSwap(3777))  # Output: 7236
print(solution.maximumSwap(98368))  # Output: 9973
