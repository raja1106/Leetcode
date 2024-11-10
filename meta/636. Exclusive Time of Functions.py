from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        exclusive_times = [0] * n
        stack = []
        # Store a pointer to the current time (initially set to an invalid time).
        prev_time = 0

        for log in logs:
            function_id, action, timestamp = log.split(":")
            function_id = int(function_id)
            timestamp = int(timestamp)

            if action == "start":
                # If there's an ongoing function, update its exclusive time.
                if stack:
                    exclusive_times[stack[-1]] += timestamp - prev_time
                stack.append(function_id)
                prev_time = timestamp
            else:  # action == "end"
                function_id = stack.pop()
                # Calculate the time spent by the current function from its start to the current timestamp and
                # update its exclusive time. The +1 accounts for the inclusive nature of the end time.
                exclusive_times[function_id] += timestamp - prev_time + 1

                # Update the current time to the end time + 1 since the next time unit
                # will indicate the start of the next event.
                prev_time = timestamp + 1

        # Return the list of calculated exclusive times.
        return exclusive_times
