https://leetcode.com/problems/fibonacci-number/description/

# Approach 1 - Using Recurssion
# time complexity - 2^n
class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)


# time complexity - O(n) Linear
# space complexity - O(n)

class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        a,b = 0 , 1
        sum_fib = 0

        while n>1:
            sum_fib = a + b
            a = b
            b = sum_fib
            n -= 1
        
        return sum_fib
