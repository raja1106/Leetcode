from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        zero_position = -1

        if nums[0] == 0:
            nums = nums[1:]
            zero_position = 0

        prefix_products = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] != 0:
                prefix_products.append(prefix_products[i - 1] * nums[i])
            else:
                if zero_position != -1:
                    return [0] * length
                zero_position = i
                prefix_products.append(prefix_products[i - 1])

        result = [0] * length
        total_product = prefix_products[-1]

        if zero_position != -1:
            result[zero_position] = total_product
            return result

        for i in range(len(nums)):
            result[i] = total_product // nums[i]

        return result


class Solution_1:#Time: O(n)  Space: O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array_length = len(nums)
        prefix_products = [1] * array_length
        suffix_products = [1] * array_length
        for i in range(1, array_length):
            prefix_products[i] = nums[i - 1] * prefix_products[i - 1]
        for i in range(array_length - 2, -1, -1):
            suffix_products[i] = nums[i + 1] * suffix_products[i + 1]
        result = []
        for i in range(array_length):
            result.append(prefix_products[i] * suffix_products[i])
        return result


class Solution_2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array_length = len(nums)
        prefix = 1
        suffix = 1
        result = [1] * array_length

        for i in range(1, array_length):
            prefix *= nums[i - 1]
            result[i] *= prefix

            suffix_i = array_length - i - 1
            suffix *= nums[suffix_i + 1]
            result[suffix_i] *= suffix

        return result