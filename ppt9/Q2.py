# Given a number n, find the sum of the first natural numbers.

# **Example 1:**

# Input: n = 3 

# Output: 6

# **Example 2:**

# Input  : 5 

# Output : 15

def sumOfFirstnNatural(n:int)-> int:
    if n ==1:
        return 1
    return n+sumOfFirstnNatural(n-1)

print(sumOfFirstnNatural(5))
