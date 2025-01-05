from collections import defaultdict, deque
from typing import List

class Solution:
    def numOfMinutes_BFS(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Create a mapping of manager to employees
        manager_to_employee_mapping = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:  # Skip the head manager
                manager_to_employee_mapping[manager[i]].append(i)

        # BFS using a queue
        queue = deque()
        queue.append((headID, 0))  # Start with the head manager, time taken so far is 0
        max_mins = 0

        # Process the queue
        while queue:
            current_mgr, current_time = queue.popleft()

            # Update the maximum time needed
            max_mins = max(max_mins, current_time)

            # Process all the employees of the current manager
            for employee in manager_to_employee_mapping[current_mgr]:
                # Add employee to queue with updated time
                queue.append((employee, current_time + informTime[current_mgr]))

        return max_mins


from collections import defaultdict
from typing import List


class Solution_DFS:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Create the manager-to-employee mapping
        manager_to_employee_mapping = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                manager_to_employee_mapping[manager[i]].append(i)

        max_mins = 0

        # DFS function to traverse the hierarchy
        def dfs(manager_id, time_so_far):
            nonlocal max_mins
            # Update the maximum time
            max_mins = max(max_mins, time_so_far)
            # Traverse the employees of the current manager
            for employee_id in manager_to_employee_mapping[manager_id]:
                dfs(employee_id, time_so_far + informTime[manager_id])

        # Start DFS from the head manager with initial time 0
        dfs(headID, 0)

        return max_mins
