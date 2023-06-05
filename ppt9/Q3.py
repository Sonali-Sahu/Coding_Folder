# Given a positive integer, N. Find the factorial of N. 

# **Example 1:**

# Input: N = 5 

# Output: 120

# **Example 2:**

# Input: N = 4

# Output: 24


def factN(n:int)->int:
    if n == 1:
        return 1
    return n * factN(n-1)

print(factN(4))
