from typing import List

"""
Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if not digits:
            return []
        phone_dict = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def get_words_from_phone_number_util(i: int, slate: List[str]) -> None:

            # Base case: If the index reaches the end of digits, append the current combination.
            if i == len(digits):
                result.append(''.join(slate))
                return

            # Recursive case: Iterate through the letters corresponding to the current digit.
            for choice in phone_dict[digits[i]]:
                slate.append(choice)
                get_words_from_phone_number_util(i + 1, slate)
                slate.pop()

        get_words_from_phone_number_util(0, [])
        return result


if __name__ == "__main__":
    # obj = Solution()
    print(Solution.letter_combinations('23'))

# pytest poetry  Poetry run  my_file.py















