from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_length = min(len(s) for s in strs)

        common_prefix = []

        for k in range(min_length):
            current_letter = strs[0][k]
            if all(s[k] == current_letter for s in strs):
                common_prefix.append(current_letter)
            else:
                break

        return ''.join(common_prefix)
