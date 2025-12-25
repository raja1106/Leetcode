class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        i = 0

        def parse_number(idx):
            k = idx

            while k < len(s) and s[k].isdigit():
                k += 1
            new_number = int(s[idx:k])
            return (k - 1, new_number)

        while i < len(s):
            if s[i].isdigit():
                new_index, new_number = parse_number(i)
                i = new_index
                st.append(new_number)
            elif s[i] == '[':
                st.append(s[i])
            elif s[i] == ']':
                parts = []
                while st and st[-1] != '[':
                    parts.append(st.pop())
                st.pop()  # remove '['

                partial_string = ''.join(reversed(parts))

                repeat_count = st.pop() if st else 1
                st.append(repeat_count * partial_string)
            else:
                st.append(s[i])
            i += 1

        return ''.join(st)


class Solution_AnotherApproach:
    def decodeString(self, s: str) -> str:
        """
        "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
        """
        n = len(s)
        i = 0
        st = []

        def parse_number(j):
            k = j
            while k < n:
                if s[k].isdigit():
                    k += 1
                else:
                    break
            return (s[j:k], k - 1)

        def parse_char(j):
            k = j
            while k < n:
                if s[k].isalpha():
                    k += 1
                else:
                    break
            return (s[j:k], k - 1)

        while i < n:
            if s[i].isdigit():
                number_str, idx = parse_number(i)
                st.append(number_str)
                i = idx
            elif s[i].isalpha():
                char_str, idx = parse_char(i)
                if st and st[-1].isalpha():
                    st[-1] = st[-1] + char_str
                else:
                    st.append(char_str)
                i = idx
            elif s[i] == '[':
                st.append(s[i])
            elif s[i] == ']':
                char_str = st.pop()
                if st:
                    st.pop()  # [
                    num_value = int(st.pop())
                    new_str = char_str * num_value
                    if st and st[-1].isalpha():
                        st[-1] = st[-1] + new_str
                    else:
                        st.append(new_str)
            i += 1

        return ''.join(st)







