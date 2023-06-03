# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.


class Solution:
    def reverseWords(self, s: str) -> str:
        s_lis = list(map(str,s.split(" ")))
        result = " ".join(x[::-1] for x in s_lis)
        return result
