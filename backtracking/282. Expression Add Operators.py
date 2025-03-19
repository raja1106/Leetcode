from typing import List

from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        self.helper(0, num, [], 0, 0, target, result)
        return result

    def helper(self, index, num, slate, current_value, previous_value, target, result):
        if index == len(num):
            if current_value == target:
                result.append(''.join(slate))
            return

        for j in range(index, len(num)):

            current_num_str = num[index:j + 1]
            current_num = int(current_num_str)

            # Skip leading zeros
            if len(current_num_str) > 1 and current_num_str[0] == '0':
                break

            if index == 0:
                # First number, no operator
                self.helper(j + 1, num, slate + [current_num_str], current_num, current_num, target, result)
            else:
                # Addition
                slate.append('+')
                slate.append(current_num_str)
                self.helper(j + 1, num, slate, current_value + current_num, current_num, target, result)
                slate.pop()
                slate.pop()
                # Subtraction
                slate.append('-')
                slate.append(current_num_str)
                self.helper(j + 1, num, slate, current_value - current_num, -current_num, target, result)
                slate.pop()
                slate.pop()
                # Multiplication
                slate.append('*')
                slate.append(current_num_str)
                self.helper(j + 1, num, slate, current_value - previous_value + previous_value * current_num,
                            previous_value * current_num, target, result)
                slate.pop()
                slate.pop()


class Solution_Another_One:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        self.helper(0, num, [], 0, 0, target, result)
        return result
    def helper(self, i, num, slate, current_value, previous_value, target, result):
        if i == len(num):
            if current_value == target:
                result.append(''.join(slate))
            return
        for j in range(i, len(num)):
            # Skip any number that starts with zero and has more than one digit
            if j > i and num[i] == '0':
                break
            current_num_str = num[i:j + 1]
            current_num = int(current_num_str)

            if i == 0:
                # First number, no operator
                self.helper(j + 1, num, slate + [current_num_str], current_num, current_num, target, result)
            else:
                # Addition
                self.helper(j + 1, num, slate + ['+', current_num_str], current_value + current_num, current_num,
                            target, result)
                # Subtraction
                self.helper(j + 1, num, slate + ['-', current_num_str], current_value - current_num, -current_num,
                            target, result)
                # Multiplication
                self.helper(j + 1, num, slate + ['*', current_num_str],
                            current_value - previous_value + previous_value * current_num, previous_value * current_num,
                            target, result)


from typing import List

class Solution_With_Division:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        self.helper(0, num, [], 0, 0, target, result)
        return result

    def helper(self, index, num, slate, current_value, previous_value, target, result):
        # If we've used all digits, check if we've reached the target.
        if index == len(num):
            if current_value == target:
                result.append(''.join(slate))
            return

        # Try all possible splits from 'index' onward.
        for j in range(index, len(num)):
            current_num_str = num[index:j + 1]
            # Convert the substring to integer.
            current_num = int(current_num_str)

            # Skip multi-digit numbers that start with '0'
            if len(current_num_str) > 1 and current_num_str[0] == '0':
                break

            # If this is the first number in the expression, just set it (no operator).
            if index == 0:
                self.helper(j + 1, num, slate + [current_num_str], current_num, current_num, target, result)
            else:
                # Addition
                slate.append('+')
                slate.append(current_num_str)
                self.helper(j + 1, num, slate,
                            current_value + current_num,
                            current_num,
                            target, result)
                slate.pop()
                slate.pop()

                # Subtraction
                slate.append('-')
                slate.append(current_num_str)
                self.helper(j + 1, num, slate,
                            current_value - current_num,
                            -current_num,
                            target, result)
                slate.pop()
                slate.pop()

                # Multiplication
                slate.append('*')
                slate.append(current_num_str)
                self.helper(j + 1, num, slate,
                            current_value - previous_value + (previous_value * current_num),
                            previous_value * current_num,
                            target, result)
                slate.pop()
                slate.pop()

                # Division (only if current_num != 0).
                # Optionally, require exact division (no remainder) by checking
                # previous_value % current_num == 0.
                if current_num != 0 and previous_value % current_num == 0:
                    slate.append('/')
                    slate.append(current_num_str)
                    new_factor = previous_value // current_num
                    new_value = current_value - previous_value + new_factor
                    self.helper(j + 1, num, slate, new_value, new_factor, target, result)
                    slate.pop()
                    slate.pop()


class Solution:
    def countOperators(self, num: str, target: int) -> int:
        n = len(num)
        memo = {}  # Key: (index, current_sum, previous_value) -> Value: count of valid expressions

        def dfs(index: int, current_sum: int, previous_value: int) -> int:
            """
            Returns how many valid expressions can be formed from num[index:]
            such that the overall expression value becomes 'target' when
            combined with the partial expression leading to (current_sum, previous_value).
            """

            # If we've consumed all digits, check if we matched the target
            if index == n:
                return 1 if current_sum == target else 0

            # Check memo
            key = (index, current_sum, previous_value)
            if key in memo:
                return memo[key]

            total_count = 0
            # Try all possible splits for the next number
            for j in range(index, n):
                # Skip multi-digit numbers with leading '0'
                if j > index and num[index] == '0':
                    break

                current_num_str = num[index:j+1]
                current_num = int(current_num_str)

                # If this is the first number (no operator yet), just initialize
                if index == 0:
                    total_count += dfs(j+1, current_num, current_num)
                else:
                    # Addition
                    total_count += dfs(j+1, current_sum + current_num, current_num)

                    # Subtraction
                    total_count += dfs(j+1, current_sum - current_num, -current_num)

                    # Multiplication
                    # Undo the previous_value in current_sum, then add (previous_value * current_num)
                    new_sum = current_sum - previous_value + (previous_value * current_num)
                    total_count += dfs(j + 1, new_sum, previous_value * current_num)

                    # Division (only if current_num != 0 and it divides evenly)
                    if current_num != 0 and previous_value % current_num == 0:
                        new_factor = previous_value // current_num
                        new_sum = current_sum - previous_value + new_factor
                        total_count += dfs(j+1, new_sum, new_factor)

            memo[key] = total_count
            return total_count

        return dfs(0, 0, 0)
