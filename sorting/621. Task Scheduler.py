import heapq
from typing import List
from collections import Counter
"""
*****Need to Practise both solutions****

You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

Return the minimum number of intervals required to complete all tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.


"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_map = Counter(tasks)
        max_heap = [-count for count in count_map.values()]
        heapq.heapify(max_heap)
        time = 0
        while max_heap:
            cycle = n + 1
            store = []
            task_count = 0
            # execute tasks in ech cycle

            while cycle > 0 and max_heap:
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

    def leastInterval_neetcode(self, tasks: List[str], n: int) -> int:
        count_map = Counter(tasks)
        max_heap = [-count for count in count_map.values()]
        heapq.heapify(max_heap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while max_heap or q:
            time += 1

            if max_heap:
                cnt = -heapq.heappop(max_heap) - 1
                if cnt > 0:
                    q.append([cnt, time + n])
            else:
                time = q[0][1]

            if q and q[0][1] == time:
                heapq.heappush(max_heap, -q.popleft()[0])

        return time
