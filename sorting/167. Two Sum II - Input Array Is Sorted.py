class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right =0,len(numbers)-1

        while left < right:
            current_sum = numbers[left]+numbers[right]
            if current_sum == target:
                return [left+1,right+1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []


class Solution_BinarySearch:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        for i in range(n):
            complement = target - numbers[i]
            left = i + 1
            right = n - 1

            # Binary search for complement
            while left <= right:
                mid = left + (right - left) // 2

                if numbers[mid] == complement:
                    return [i + 1, mid + 1]
                elif numbers[mid] < complement:
                    left = mid + 1
                else:
                    right = mid - 1

        return [-1, -1]
