class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        # Start with the first sequence
        current_seq = "1"

        for _ in range(2, n + 1):
            next_seq = []
            count = 1

            # Iterate through the current sequence to build the next one
            for i in range(1, len(current_seq)):
                if current_seq[i] == current_seq[i - 1]:
                    count += 1
                else:
                    # Append the count and the digit
                    next_seq.append(str(count))
                    next_seq.append(current_seq[i - 1])
                    count = 1

            # Append the count and the last digit
            next_seq.append(str(count))
            next_seq.append(current_seq[-1])

            # Update current_seq to be the newly formed sequence
            current_seq = ''.join(next_seq)

        return current_seq
