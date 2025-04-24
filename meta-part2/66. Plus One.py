class Solution_Efficient_First:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
class Solution_Efficient_Second:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        result = []
        for val in reversed(digits):
            total = carry+val
            carry,digit = divmod(total,10)
            result.append(digit)
        if carry:
            result.append(carry)
        return result[::-1]

class Solution_Not_Efficient:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_str = ''.join([str(d) for d in digits])
        digit_val = int(digits_str)
        result_str = str(digit_val+1)
        return [int(s) for s in result_str]
