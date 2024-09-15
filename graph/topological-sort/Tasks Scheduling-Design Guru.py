'''
Problem Statement
There are ‘N’ num_tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite num_tasks which need to be completed before it can be scheduled.

Given the number of num_tasks and a list of prerequisite pairs, find out if it is possible to schedule all the num_tasks.

Examples
Example 1:

Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: true
Explanation: A possible scheduling of num_tasks is: [0 1 4 3 2 5]
Example 2:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: true
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish before '2' can be scheduled. One possible scheduling of num_tasks is: [0, 1, 2]
Example 3:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
Output: false
Explanation: The num_tasks have a cyclic dependency, therefore they cannot be scheduled.

'''

from collections import defaultdict


class Solution:
    def isSchedulingPossible(self, num_tasks, prerequisites):
        # Edge case: No num_tasks, return True
        if num_tasks == 0:
            return True
        visited = [False] * num_tasks
        topological_order = []
        graph = defaultdict(list)
        for src, dst in prerequisites:
            graph[src].append(dst)
        on_stack = set()
        def has_cycle(node: int) -> bool:
            visited[node] = True
            on_stack.add(node)
            for neighbour in graph[node]:
                if neighbour in on_stack:  # Cycle detected (back edge)
                    return True
                if not visited[neighbour]:
                    if has_cycle(neighbour):  # If a cycle is detected, return True
                        return True
            # Add node to the topological order and remove it from the recursion stack
            topological_order.append(node)
            on_stack.remove(node)
            return False

        # Perform DFS on all nodes
        for u in range(num_tasks):
            if not visited[u]:
                if has_cycle(u):  # If a cycle is detected, return False
                    return False  # return [] if topological_order is requested
        # If no cycle is detected, return True indicating valid scheduling is possible
        return True  # topological_order[::-1]
