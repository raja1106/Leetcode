import heapq
from typing import List
from collections import Counter
"""
*****Need to Practise both solutions****

You are given an array of CPU num_tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical num_tasks must be separated by at least n intervals due to cooling time.

Return the minimum number of intervals required to complete all num_tasks.

 

Example 1:

Input: num_tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

Example 2:

Input: num_tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.


"""

from collections import Counter, deque
from heapq import heapify, heappop, heappush
from typing import List


class Solution_Best_Approach:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Edge Case: No tasks
        if not tasks:
            return 0

        # Count occurrences of each task
        task_count = Counter(tasks)

        # Max heap (negative frequencies for max heap behavior)
        max_heap = [-cnt for cnt in task_count.values()]
        heapify(max_heap)

        # Queue to store tasks in cooldown (format: (remaining_count, next_available_time))
        wait_queue = deque()

        # Time counter
        time = 0

        while max_heap or wait_queue:
            if max_heap:
                # Execute the most frequent task
                time += 1
                count = -heappop(max_heap)  # Extract highest frequency task
                count -= 1

                # If the task still has occurrences, add it to cooldown
                if count > 0:
                    wait_queue.append((count, time + n))
            else:
                # Jump directly to the next available task's time if idle
                time = wait_queue[0][1]

            # Check and release any tasks from cooldown
            while wait_queue and wait_queue[0][1] <= time:
                cnt_ready, _ = wait_queue.popleft()
                heappush(max_heap, -cnt_ready)

        return time


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_map = Counter(tasks)
        max_heap = [-count for count in count_map.values()]
        heapq.heapify(max_heap)
        time = 0
        while max_heap:
            cycle = n
            store = []
            task_count = 0
            # execute num_tasks in ech cycle

            while cycle >= 0 and max_heap:
                count_freq = -heapq.heappop(max_heap)
                count_freq -= 1
                if count_freq > 0:
                    store.append(count_freq)
                task_count += 1
                cycle -= 1

                # Restore updated frequencies to the heap
            for x in store:
                heapq.heappush(max_heap, -x)
            time += task_count if not max_heap else n + 1
        return time
