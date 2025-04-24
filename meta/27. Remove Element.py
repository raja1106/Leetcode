class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insert_position = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            else:
                nums[insert_position] = nums[i]
                insert_position += 1

        return insert_position # 2 2
