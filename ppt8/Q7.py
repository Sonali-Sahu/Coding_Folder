# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string
# inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.


class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        num = 0
        res = ''

        for ch in s:
            if ch.isnumeric():
                num = num * 10 + int(ch)
            elif ch == '[':
                st.append(res)
                st.append(num)
                res = ''
                num = 0
            elif ch == ']':
                cnt = st.pop()
                prev = st.pop()
                res = prev + cnt * res
            else:
                res += ch
        return res
