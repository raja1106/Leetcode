from typing import List, Union


class NestedInteger:
    def isInteger(self) -> bool:
        # Returns True if this NestedInteger holds a single integer, rather than a nested list
        pass

    def getInteger(self) -> int:
        # Returns the single integer that this NestedInteger holds, if it holds a single integer
        # The result is undefined if this NestedInteger holds a nested list
        pass

    def getList(self) -> List['NestedInteger']:
        # Returns the nested list that this NestedInteger holds, if it holds a nested list
        # The result is undefined if this NestedInteger holds a single integer
        pass


class Solution:
    def depth_sum(self, nested_list: List[NestedInteger]) -> int:
        """
        Calculate the sum of all integers in the nested list weighted by their depth.

        :param nested_list: List[NestedInteger] - a list of NestedInteger
        :return: int - depth sum of input nested list
        """

        def dfs(current_list: List[NestedInteger], current_depth: int) -> int:
            """
            Recursive helper function to calculate the depth sum.

            :param current_list: List[NestedInteger] - the current level's nested list
            :param current_depth: int - the current depth level
            :return: int - depth sum for the current level
            """
            current_depth_sum = 0  # Initialize the depth sum for the current level

            # Loop through each item in the current nested list
            for item in current_list:
                if item.isInteger():
                    # If the item is an integer, add its value times the current depth
                    current_depth_sum += item.getInteger() * current_depth
                else:
                    # If the item is a list, recursively call dfs to calculate its depth sum
                    current_depth_sum += dfs(item.getList(), current_depth + 1)

            return current_depth_sum  # Return the calculated depth sum for this level

        return dfs(nested_list, 1)

# Example usage:
# Assuming NestedInteger is properly implemented
# solution = Solution()
# nested_list = [...]  # Some list of NestedInteger
# print(solution.depth_sum(nested_list))

# Nested list: [1, [2, 3], 4, [5, [6]]]
#nested_list = [NestedInteger(1), NestedInteger([NestedInteger(2), NestedInteger(3)]), NestedInteger(4), NestedInteger([NestedInteger(5), NestedInteger([NestedInteger(6)])])]
#print(solution.depth_sum(nested_list))  # Output: 44
# Explanation: 1*1 + (2*2 + 3*2) + 4*1 + (5*2 + 6*3) = 1 + 10 + 4 + 29 = 44
