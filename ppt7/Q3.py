# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        result = []
        carry = i = 0
        l1 , l2 = len(num1), len(num2)
        l3 = max(l1, l2)
        while i < l3 or carry:
            dig1 = (ord(num1[i]) - ord('0')) if i < l1 else 0
            dig2 = (ord(num2[i]) - ord('0')) if i < l2 else 0
            sm = ((dig1 + dig2 + carry) % 10)
            carry = ((dig1 + dig2 + carry) // 10)
            result.append(str(sm))
            i += 1
        return ''.join(result[::-1])
