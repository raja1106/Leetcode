class Solution:
    def simplifyPath(self, path: str) -> str:
        # Initialize an empty list to use as a stack
        stack = []

        # Split the path by "/", iterate over each part
        for part in path.split('/'):
            # If the part is an empty string or a ".", simply continue to the next part
            if not part or part == '.':
                continue
            # If the part is "..", pop from the stack if it's not empty
            elif part == '..':
                if stack:
                    stack.pop()
            # Otherwise, add the part to the stack
            else:
                stack.append(part)

        # Join the stack elements to form the simplified path and prepend with "/"
        simplified_path = '/' + '/'.join(stack)
        return simplified_path

    class Solution:
        def simplifyPath(self, path: str) -> str:
            # Stack to store the valid parts of the path
            stack = []

            # Split the path by "/" and iterate over each component
            for part in path.split('/'):
                if part == '..':
                    if stack:  # Go up one directory level if possible
                        stack.pop()
                elif part and part != '.':  # Ignore empty strings and current directory symbols
                    stack.append(part)

            # Join the stack to form the simplified path
            return '/' + '/'.join(stack)


class Solution1:
    def simplifyPath(self, path: str) -> str:
        # Stack to store the valid parts of the path
        stack = []

        # Split the path by "/" and iterate over each component
        for part in path.split('/'):
            if part == '..':
                if stack:  # Go up one directory level if possible
                    stack.pop()
            elif part and part != '.':  # Ignore empty strings and current directory symbols
                stack.append(part)

        # Join the stack to form the simplified path
        return '/' + '/'.join(stack)

