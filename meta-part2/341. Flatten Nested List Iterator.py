class NestedInteger:
    def __init__(self, value=None):
        if isinstance(value, int):
            self._integer = value
            self._list = None
        elif isinstance(value, list):
            self._integer = None
            self._list = [NestedInteger(x) if not isinstance(x, NestedInteger) else x for x in value]
        else:
            self._integer = None
            self._list = []

    def isInteger(self) -> bool:
        return self._integer is not None

    def getInteger(self) -> int:
        return self._integer

    def getList(self) -> ['NestedInteger']:
        return self._list

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # Stack will store tuples of (list, current index)
        # Start with the outermost list and index 0
        self.stack = [(nestedList, 0)]

    def next(self) -> int:
        # Ensure hasNext() moves us to a valid integer
        if self.hasNext():
            nestedList, i = self.stack[-1]
            self.stack[-1] = (nestedList, i + 1)  # Move index forward
            return nestedList[i].getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            nestedList, i = self.stack[-1]
            if i == len(nestedList):
                self.stack.pop()  # Finished this list
            else:
                elem = nestedList[i]
                if elem.isInteger():
                    return True
                # Otherwise, it's a nested list: drill down
                self.stack[-1] = (nestedList, i + 1)  # Advance current index
                self.stack.append((elem.getList(), 0))
        return False
