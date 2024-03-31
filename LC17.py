class LC17:
    def letterCombinations(self, digits):
        # If the input is empty, immediately return an empty answer array
        if len(digits) == 0:
            return []

        # Map all the digits to their corresponding letters
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backtrack(index, path):
            # If the path is the same length as digits, we have a complete combination
            if len(path) == len(digits):
                combinations.append("".join(path))
                return  # Backtrack

            # Get the letters that the current digit maps to, and loop through them
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                # Add the letter to our current path
                path.append(letter)
                # Move on to the next digit
                backtrack(index + 1, path)
                # Backtrack by removing the letter before moving onto the next
                path.pop()

        # Initiate backtracking with an empty path and starting index of 0
        combinations = []
        backtrack(0, [])
        return combinations

    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        min_heap = []
        for i in range(n):
            min_heap.append([0,i]) #end_time,room_number
        heapify(min_heap)
        count = [0] * n
        # meeting_count = Counter()
        q = deque()

        for start_time, end_time in meetings:
            temp=[]
            while min_heap and min_heap[0] <= start_time:
                temp.append(heappop(min_heap))

            if min_heap:
                room_index = heappop(min_heap)
                count[room_index] += 1
                heappush(busy_rooms_heap, [end_time, room_index])
            else:  # No idle rooms; wait for the first available room
                earliest_end, room_index = heappop(busy_rooms_heap)
                count[room_index] += 1
                heappush(busy_rooms_heap, [earliest_end + end_time - start_time, room_index])

        # room_list = meeting_count.most_common()
        # return room_list[0][0]
        return count.index(max(count))


