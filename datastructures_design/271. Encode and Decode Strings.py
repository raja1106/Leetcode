from typing import List


class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            # Format: <length> + <separator> + <string>
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings.
        """
        res, i = [], 0

        while i < len(s):
            # Find the position of the next separator
            j = i
            while s[j] != "#":
                j += 1

            # Extract the length of the upcoming string
            length = int(s[i:j])

            # Move the pointer to the start of the actual string
            start = j + 1
            end = start + length

            # Append the slice and update our main pointer
            res.append(s[start:end])
            i = end

        return res


class Codec_Another_Approach:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        hello world --> hello-world
        """
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        "5#hello3#a#b0#"
        2:7
        """

        i = 0
        result = []
        while i < len(s):
            if s[i].isdigit():
                j = i
                while j < len(s) and s[j] != '#':
                    j += 1

                current_length = int(s[i:j])  # 3#abc5#asdfg
                i = j + 1
                if current_length == 0 and i >= len(s):
                    result.append('')
                    break
                current_part = s[i:i + current_length]
                result.append(current_part)
                i = i + current_length

        return result

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))