from typing import List


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


class Solution_2:#Time: O(n)  Space: O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        # Initialize the result array with 1s
        result = [1] * length

        # Calculate prefix products and store in result array
        prefix_product = 1
        for i in range(length):
            result[i] = prefix_product
            prefix_product *= nums[i]

        # Calculate suffix products and multiply with the result array
        suffix_product = 1
        for i in range(length - 1, -1, -1):
            result[i] *= suffix_product
            suffix_product *= nums[i]

        return result


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

