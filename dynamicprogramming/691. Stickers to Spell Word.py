class Solution_Bruteforce:

    def minStickers(self, stickers, target):
        # Convert target and stickers into Counter (frequency maps)
        target_count = Counter(target)
        stickers_count = [Counter(sticker) for sticker in stickers]

        # Initialize the minimum number of stickers needed to an infeasible high value
        min_stickers_needed = float('inf')

        def dfs(remaining_target, stickers_used):
            nonlocal min_stickers_needed

            # Base case: if there are no characters left in the target, update min_stickers_needed
            if not remaining_target:
                min_stickers_needed = min(min_stickers_needed, stickers_used)
                return

            # Optimization: if the current path already uses more stickers than the best found, backtrack
            if stickers_used >= min_stickers_needed:
                return

            # Go through each sticker and try to use it
            for sticker in stickers_count:
                # If the sticker has the first character in remaining_target, we try it
                if any(letter in sticker for letter in remaining_target):
                    # Create a new Counter for the next state after using the sticker
                    next_target = remaining_target - sticker

                    # Recursive call with the new target and increment stickers used
                    dfs(next_target, stickers_used + 1)

        # Start DFS with the initial target and 0 stickers used
        dfs(target_count, 0)
        # Return result
        return min_stickers_needed if min_stickers_needed != float('inf') else -1




class Solution_Using_memo:
    def minStickers(self, stickers, target):
        target_count = Counter(target)
        stickers_count = [Counter(sticker) for sticker in stickers]
        memo = {}

        def dfs(remaining_target):
            # Convert remaining_target to a hashable key for memoization
            target_key = tuple(sorted(remaining_target.items()))

            # Base case: if there are no characters left in the target, we need 0 stickers
            if not remaining_target:
                return 0

            # Check memoized result
            if target_key in memo:
                return memo[target_key]

            # Initialize the minimum stickers needed to an infeasible high value for this state
            min_stickers = float('inf')

            # Try each sticker and see how much it helps reduce the remaining_target
            for sticker in stickers_count:
                # If the sticker contributes to the target, try it
                if any(letter in sticker for letter in remaining_target):
                    # Create a new Counter for the next state after using the sticker
                    new_target = remaining_target - sticker
                    # Recursive call with the new target and add 1 sticker used
                    result = dfs(new_target)
                    if result != float('inf'):
                        min_stickers = min(min_stickers, result + 1)

            # Memoize and return the result for this target state
            memo[target_key] = min_stickers
            return min_stickers

        # Start DFS with the initial target and return the result
        result = dfs(target_count)
        return result if result != float('inf') else -1


from collections import Counter


class Solution_Using_Memo_2ndApproach:
    def minStickers(self, stickers, target):
        target_count = Counter(target)
        stickers_count = [Counter(sticker) for sticker in stickers]
        memo = {}

        def dfs(remaining_target):
            # Convert remaining_target to a hashable key for memoization
            target_key = tuple(sorted(remaining_target.items()))

            # Base case: if there are no characters left in the target, we need 0 stickers
            if not remaining_target:
                return 0

            # Check memoized result
            if target_key in memo:
                return memo[target_key]

            # Initialize the minimum stickers needed to an infeasible high value for this state
            min_stickers = float('inf')

            # Try each sticker and see how much it helps reduce the remaining_target
            for sticker in stickers_count:
                # If the sticker contributes to the target, try it
                if any(letter in sticker for letter in remaining_target):
                    # Create a new Counter for the next state after using the sticker
                    new_target = remaining_target.copy()
                    for letter in sticker:
                        if letter in new_target:
                            new_target[letter] -= sticker[letter]
                            if new_target[letter] <= 0:
                                del new_target[letter]

                    # Recursive call with the new target and add 1 sticker used
                    result = dfs(new_target)
                    if result != float('inf'):
                        min_stickers = min(min_stickers, result + 1)

            # Memoize and return the result for this target state
            memo[target_key] = min_stickers
            return min_stickers

        # Start DFS with the initial target and return the result
        result = dfs(target_count)
        return result if result != float('inf') else -1

"""
META Version
Problem Description:
Given a string sticker that represents the set of characters available on a single sticker and a string word that represents the target word to spell out, return the minimum number of stickers that you need to spell out word. Each sticker can be used more than once, and you have an unlimited supply of stickers.
Meta version of https://leetcode.com/problems/stickers-to-spell-word/description/


If the word cannot be spelled out using the letters on the sticker, return -1.


Note:


The sticker and word consist of lowercase English letters only.
The lengths of the sticker and word strings are both in the range [1, 1000].
Function Signature:


public int minStickers(String sticker, String word) {
}
Example 1:
Input: sticker = "ban", word = "banana"
Output: 3
Explanation: We can use 3 stickers "bana" to spell out the word "banana". Each sticker provides one "b", one "a", and one "n". Three stickers provide all the letters needed to spell out "banana".
"""

from collections import Counter
import math

def min_stickers_required(sticker: str, target_word: str) -> int:
    """
    Calculate the minimum number of stickers required to form the target word.
    Returns -1 if the target word cannot be formed using the given sticker.
    """
    # Frequency count of each character in the sticker and target word
    sticker_count = Counter(sticker)
    target_count = Counter(target_word)

    # Initialize the minimum number of stickers required
    min_stickers = 0
    for char, required_count in target_count.items():
        if char not in sticker_count:
            return -1  # If any character in target_word is missing in sticker, return -1
        # Calculate the number of stickers needed to cover the required character count
        stickers_needed_for_char = math.ceil(required_count / sticker_count[char])
        min_stickers = max(min_stickers, stickers_needed_for_char)

    return min_stickers
