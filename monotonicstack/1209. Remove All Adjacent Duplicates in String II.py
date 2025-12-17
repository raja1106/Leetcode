class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        def remove_run(char_to_remove):
            while stack and stack[-1][0] == char_to_remove:
                stack.pop()

        stack = []

        for char in s:
            if stack and stack[-1][0] == char:
                last_count = stack[-1][1]

                if last_count + 1 == k:
                    remove_run(char)
                else:
                    stack.append((char, last_count + 1))
            else:
                stack.append((char, 1))

        result_chars = [item[0] for item in stack]
        return ''.join(result_chars)

class Solution_AnotherApproach:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # each element is [char, count]

        for ch in s:
            if stack and stack[-1][0] == ch:
                # Increment count of the top run
                stack[-1][1] += 1
                # If count reaches k, remove this run
                if stack[-1][1] == k:
                    stack.pop()
            else:
                # Start a new run
                stack.append([ch, 1])

        # Rebuild the string
        return ''.join(ch * count for ch, count in stack)
