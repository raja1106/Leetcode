class Solution:
    def simplifyPath(self, path: str) -> str:
        # Initialize an empty list to use as a stack
        stack = []

        # Split the path by "/", iterate over each segment
        for segment in path.split('/'):
            # If the segment is an empty string or a ".", simply continue to the next segment
            if not segment or segment == '.':
                continue
            # If the segment is "..", pop from the stack if it's not empty
            elif segment == '..':
                if stack:
                    stack.pop()
            # Otherwise, add the segment to the stack
            else:
                stack.append(segment)

        # Join the stack elements to form the simplified path and prepend with "/"
        simplified_path = '/' + '/'.join(stack)
        return simplified_path


class Solution_In_Place_Processing_withoutSplit:
    def simplifyPath(self, path: str) -> str:
        path_stack = []
        i = 0
        n = len(path)

        while i < n:
            # Skip consecutive '/' characters
            while i < n and path[i] == '/':
                i += 1

            start = i
            # Identify the current segment (until the next '/')
            while i < n and path[i] != '/':
                i += 1

            segment = path[start:i]
            if segment in ['', '.']:
                continue
            elif segment == '..':
                if path_stack:
                    path_stack.pop()
            else:
                path_stack.append(segment)

        return '/' + '/'.join(path_stack)
