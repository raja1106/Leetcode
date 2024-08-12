class Solution:
    def removeDuplicates(self, s: str) -> str:
        if not s:
            return s

        unique_string = []

        for char in s:
            if unique_string and unique_string[-1] == char:
                unique_string.pop()
            else:
                unique_string.append(char)

        return ''.join(unique_string)
