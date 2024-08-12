class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()

        if not s:
            return False

        # Check if the first character is a sign
        if s[0] in ['+', '-']:
            s = s[1:]

        has_point, has_number, has_e = False, False, False

        for i, char in enumerate(s):
            if char in 'eE':
                # 'e' should not have appeared before, and must follow a number
                if has_e or not has_number:
                    return False
                has_e, has_number = True, False  # Reset has_number to ensure a number follows 'e'
            elif char in ['+', '-']:
                # A sign must follow an 'e'
                if i == 0 or s[i-1] not in 'eE':
                    return False
            elif char == '.':
                # A point should not appear after 'e' or if there's already a point
                if has_point or has_e:
                    return False
                has_point = True
            elif char.isdigit():
                has_number = True
            else:
                return False

        return has_number
