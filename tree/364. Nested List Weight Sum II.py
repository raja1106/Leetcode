from typing import List, Optional


class NestedInteger:
    def __init__(self, value: Optional[int] = None):
        """
        If value is provided, this NestedInteger holds a single integer.
        Otherwise, it holds a nested list.
        """
        if value is None:
            self._integer = None
            self._list = []
        else:
            self._integer = value
            self._list = None

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer,
                rather than a nested list.
        """
        return self._integer is not None

    def add(self, elem: 'NestedInteger') -> None:
        """
        Set this NestedInteger to hold a nested list and adds a nested integer to it.
        """
        if self._list is None:
            self._list = []
            self._integer = None
        self._list.append(elem)

    def setInteger(self, value: int) -> None:
        """
        Set this NestedInteger to hold a single integer.
        """
        self._integer = value
        self._list = None

    def getInteger(self) -> Optional[int]:
        """
        @return the single integer that this NestedInteger holds,
                if it holds a single integer
        @return None if this NestedInteger holds a nested list
        """
        return self._integer

    def getList(self) -> List['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds,
                if it holds a nested list
        @return empty list if this NestedInteger holds a single integer
        """
        return [] if self._list is None else self._list

    def __repr__(self):
        if self.isInteger():
            return str(self._integer)
        return str(self._list)


class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        max_depth = -1

        def calculate_max_depth(current_list, current_depth):
            max_depth = current_depth
            for list_element in current_list:
                if not list_element.isInteger():
                    local_max_depth = calculate_max_depth(list_element.getList(), current_depth + 1)
                    max_depth = max(local_max_depth, max_depth)
            return max_depth

        max_depth = calculate_max_depth(nestedList, 1)

        def dfs(current_list, current_depth):
            total = 0
            for list_element in current_list:
                x = (max_depth - current_depth + 1)

                if list_element.isInteger():
                    total += x * list_element.getInteger()
                else:
                    total += dfs(list_element.getList(), current_depth + 1)

            return total

        return dfs(nestedList, 1)


if __name__ == "__main__":
    # Example 1: [[1,1],2,[1,1]]
    first = NestedInteger()
    first.add(NestedInteger(1))
    first.add(NestedInteger(1))

    second = NestedInteger()
    second.add(NestedInteger(1))
    second.add(NestedInteger(1))

    nestedList1 = [first, NestedInteger(2), second]

    # Example 2: [1,[4,[6]]]
    inner = NestedInteger()
    inner.add(NestedInteger(6))

    middle = NestedInteger()
    middle.add(NestedInteger(4))
    middle.add(inner)

    nestedList2 = [NestedInteger(1), middle]

    sol = Solution()

    print("Input 1:", nestedList1)
    print("Output 1:", sol.depthSumInverse(nestedList1))

    print("Input 2:", nestedList2)
    print("Output 2:", sol.depthSumInverse(nestedList2))