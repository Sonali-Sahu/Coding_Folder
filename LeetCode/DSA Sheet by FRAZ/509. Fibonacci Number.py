https://leetcode.com/problems/fibonacci-number/description/

# Approach 1 - Using Recurssion
# time complexity - 2^n
class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)
