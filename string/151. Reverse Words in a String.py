class Solution:
    def reverseWords(self, s: str) -> str:
        # Convert string to char array for in-place modifications
        str_arr = list(s)

        # Step 1: Reverse entire string
        self._reverse(str_arr, 0, len(str_arr) - 1)

        # Step 2: Reverse each word
        self._reverse_words(str_arr)

        # Step 3: Clean up spaces and return the cleaned string
        return self._clean_spaces(str_arr)

    def _reverse(self, arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    def _reverse_words(self, arr):
        n = len(arr)
        start = 0
        for end in range(n):
            # Find the end of the current word
            if arr[end] == ' ':
                self._reverse(arr, start, end - 1)
                start = end + 1  # Move to the start of the next word
        # Reverse the last word
        self._reverse(arr, start, n - 1)

    def _clean_spaces(self, arr):
        n = len(arr)
        i = j = 0

        while j < n:
            # Skip spaces
            while j < n and arr[j] == ' ':
                j += 1
            # Copy non-space characters
            while j < n and arr[j] != ' ':
                arr[i] = arr[j]
                i += 1
                j += 1
            # Skip spaces to reach the next word, add only one space if there's a next word
            while j < n and arr[j] == ' ':
                j += 1
            if j < n:
                arr[i] = ' '
                i += 1

        return ''.join(arr[:i])