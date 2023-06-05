# Given an integer `n`, return *`true` if it is a power of two. Otherwise, return `false`*.

# An integer `n` is a power of two, if there exists an integer `x` such that `n == 2x`.

# using binary conversion and checking if 1 is available
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return bin(n)[2:].rstrip('0') == '1'

    
# recursion

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if (n%2!=0):
            return False
        return self.isPowerOfTwo(n/2)
