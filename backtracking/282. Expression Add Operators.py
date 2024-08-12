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
            # Skip numbers with leading zeros
            if j > index and num[index] == '0':
                break

            current_num_str = num[index:j + 1]
            current_num = int(current_num_str)

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


class Solution:
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


