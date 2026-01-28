class StringIterator_Optimized:
    def __init__(self, compressedString: str):
        self.s = compressedString
        self.ptr = 0
        self.curr_char = ''
        self.curr_count = 0

    def next(self) -> str:
        if not self.hasNext():
            return ' '  # Must be a space per LC specs

        # Only parse the next segment if the current one is finished
        if self.curr_count == 0:
            self.curr_char = self.s[self.ptr]
            self.ptr += 1

            # Extract the multi-digit number
            num_start = self.ptr
            while self.ptr < len(self.s) and self.s[self.ptr].isdigit():
                self.ptr += 1
            self.curr_count = int(self.s[num_start:self.ptr])

        self.curr_count -= 1
        return self.curr_char

    def hasNext(self) -> bool:
        # It has next if we are still counting down a char
        # OR if there's more string to parse
        return self.curr_count > 0 or self.ptr < len(self.s)

class StringIterator_Naive:

    def __init__(self, compressedString: str):
        self.compressedString = compressedString
        self.arr = []
        self.current_parsing_index = 0

    def _parse_str(self, s, idx):
        j = idx
        while j < len(s) and s[j].isdigit():
            j += 1
        return (j, int(s[idx:j]))

    def next(self) -> str:
        if self.arr:
            return self.arr.pop()

        if self.current_parsing_index < len(self.compressedString) and self.compressedString[
            self.current_parsing_index].isalpha():
            next_char = self.compressedString[self.current_parsing_index]
            next_index, next_count = self._parse_str(self.compressedString, self.current_parsing_index + 1)
            self.arr = list(next_char * next_count)
            self.current_parsing_index = next_index
            return self.arr.pop()

        return " "

    def hasNext(self) -> bool:
        if self.arr:
            return True
        i = self.current_parsing_index
        while i < len(self.compressedString) and not self.compressedString[i].isalpha():
            i += 1

        return i < len(self.compressedString)

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()