class Solution_naive:
    def removeDuplicates(self, nums: List[int]) -> int:
        current =1
        k = 1
        current_element = nums[0]
        current_element_count = 1
        while current < len(nums):
            if nums[current] ==  current_element:
                current_element_count += 1
                if current_element_count > 2:
                    current += 1
                else:
                    nums[k] = nums[current]
                    current += 1
                    k += 1
            else:
                current_element = nums[current]
                current_element_count = 1
                nums[k] = nums[current]
                k += 1
                current += 1
        print(k)
        return k


class Solution_Algo_monster:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Pointer to track the position for the next valid element
        write_index = 0

        # Iterate through each element in the array
        for current_num in nums:
            # Allow element if:
            # 1. We have less than 2 elements (write_index < 2), OR
            # 2. Current element is different from the element 2 positions back
            if write_index < 2 or current_num != nums[write_index - 2]:
                # Place the current element at the write position
                nums[write_index] = current_num
                # Move write pointer forward
                write_index += 1

        # Return the length of the modified array
        return write_index
