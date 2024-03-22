from typing import List
from collections import Counter, deque
from heapq import heapify, heappop, heappush

import heapq
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            while i != nums[i]:
                d = nums[i]

                if d<len[nums]:
                    nums[d],nums[i]=nums[i],nums[d]
                else:
                    break



        return nums

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return point[0]**2 + point[1]**2
        max_heap =[]
        result=[]
        for i in range(len(points)):
            heapq.heappush((distance(points[i]),points[i]))
            if len(max_heap) > k:
                max_heap.pop()

        for element in max_heap:
            result.append(element[1])
'''
76. Minimum Window Substring
Solved
Hard
Topics
Companies
Hint
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t)>len(s):
            return ''
        t_map = Counter(t)
        k = len(t)
        s_map={}

        for i in range(k):
            s_map[s[i]] = s_map.get(s[i], 0)+1

        if t_map == s_map:
            return s[:k]
        min_window = len(s)
        ans=''
        left=0
        def ismatching(s_map,t_map):

            for char,count in t_map.items():
                if char not in s_map and s_map[char] < count:
                    return False

            return True

        for i in range(k,len(s)):
            s_map[s[i]] = s_map.get(s[i], 0) + 1
            while left < i and ismatching(s_map,t_map):
                if min_window >= i-left+1:
                    ans = s[left:i + 1]
                    min_window= i-left+1
                s_map[s[left]] = s_map.get(s[left], 0)-1
                left += 1

        return ans

    def minWindow_mons(self, source: str, target: str) -> str:
        # Create a counter for the target to keep a record of each character's frequency
        target_counter = Counter(target)
        window_counter = Counter()  # This will keep a count of characters in the current window
        valid_char_count = 0  # Number of characters that meet the target criteria
        left = 0  # Left pointer to shrink the window
        min_left = -1  # Left boundary index of the minimum window
        min_size = inf  # Initialize min_size to positive infinity

        # Iterate over each character in the source string
        for i, char in enumerate(source):
            # Include current character in the window
            window_counter[char] += 1
            # If the current character is needed and the window contains enough of this character
            if target_counter[char] >= window_counter[char]:
                valid_char_count += 1

            # If the window has all the characters needed
            while valid_char_count == len(target):
                # If this window is smaller than the minimum so far, update minimum size and index
                if i - left + 1 < min_size:
                    min_size = i - left + 1
                    min_left = left

                # If the character at the left pointer is less frequent in the window than in the target,
                # reducing it further would break the window condition
                if target_counter[source[left]] >= window_counter[source[left]]:
                    valid_char_count -= 1

                # Shrink the window from the left
                window_counter[source[left]] -= 1
                left += 1

        # If no window meets the criteria, return an empty string
        return '' if min_left < 0 else source[min_left:min_left + min_size]


    def findDuplicate(self, nums: List[int]) -> int:

        def swap(s,d):
            if nums[s] == nums[d]:
                return nums[s]
            nums[s],nums[d] = nums[d],nums[s]

        for i in range(len(nums)):
            while nums[i] != i+1:
                d=nums[i]-1
                if d >len(nums)-1:
                    break
                swap(i,d)

    def totalFruit(self, fruits: List[int]) -> int:
        max_count=-1
        bucket1=-1


        for i in range(len(fruits)):
            local_count = 0
            bucket1 = fruits[i]
            bucket2 = -1

            for j in range(i+1, len(fruits)):
                if fruits[j] == bucket1:
                    local_count += 1
                    continue

                if bucket2 == -1:
                    bucket2 = fruits[j]
                    local_count += 1
                    continue

                if fruits[j] == bucket2:
                    local_count += 1
                else:
                    break
            max_count = max(max_count,local_count)
            return max_count

    def totalFruit_usingsort(self, fruits: List[int]) -> int:
        fruit_map =Counter()
        left =0
        max_size=-1
        for i in range(len(fruits)):
            fruit_map[fruits[i]] += 1

            while left<i and len(fruit_map)>2:
                fruit_map[fruits[left]] -= 1
                if fruit_map[fruits[left]] == 0:
                    del fruit_map[fruits[left]]
                left += 1
            max_size =max(max_size,i-left+1)

        return max_size





obj=Solution()
print(obj.test([2,3,4,5]))

