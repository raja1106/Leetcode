from typing import List

from typing import List


class Solution1:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        Given a list of integers `nums` and an integer `k`, return True if there is a continuous subarray
        of size at least two that sums up to a multiple of `k`. Otherwise, return False.

        Args:
        nums (List[int]): List of integers.
        k (int): The integer to check multiples of.

        Returns:
        bool: True if such a subarray exists, False otherwise.
        """
        if len(nums) < 2:
            return False

        # Handle the edge case where k is 0
        if k == 0:
            for i in range(1, len(nums)):
                if nums[i] == 0 and nums[i - 1] == 0:
                    return True
            return False

        prefix_sum_map = {0: -1}  # Store the index of the prefix sum remainders
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            remainder = prefix_sum % k

            if remainder in prefix_sum_map:
                if i - prefix_sum_map[remainder] >= 2:
                    return True
            else:
                prefix_sum_map[remainder] = i

        return False


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        mod_set = set()
        mod_set.add(0)

        prefix_sum = nums[0] % k

        for i in range(1, len(nums)):
            old_sum = prefix_sum
            prefix_sum = (prefix_sum + nums[i]) % k

            if prefix_sum in mod_set:
                return True

            mod_set.add(old_sum)

        return False

    def checkSubarraySum_Approach2(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        mod_set = set()
        mod_set.add(0)

        ps = nums[0]
        for i in range(1, len(nums)):
            old_mod = ps % k
            ps += nums[i]

            current_mod = ps % k

            if current_mod in mod_set:
                return True

            mod_set.add(old_mod)

        return False

    def checkSubarraySum_AlgoMonster(self, nums: List[int], k: int) -> bool:
        # Initialize the prefix sum as zero
        prefix_sum = 0

        # A dictionary to keep track of the earliest index where
        # a particular modulus (prefix_sum % k) is found.
        mod_index_map = {0: -1}  # The modulus 0 is at the "imaginary" index -1

        # Iterate over the list of numbers
        for index, value in enumerate(nums):
            # Update the prefix sum with the current value
            prefix_sum += value

            # Get the modulus of the prefix sum with 'k'
            modulus = prefix_sum % k

            # If the modulus has been seen before and the distance between
            # the current index and the earlier index of the same modulus
            # is at least 2, we found a subarray sum that's multiple of k
            if modulus in mod_index_map and index - mod_index_map[modulus] >= 2:
                return True

            # Store the index of this modulus if it's not seen before
            if modulus not in mod_index_map:
                mod_index_map[modulus] = index

        # No subarray found that sums up to a multiple of k
        return False