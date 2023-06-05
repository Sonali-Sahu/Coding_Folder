# Given an array of integers **arr**, the task is to find maximum 
# element of that array using recursion.

# **Example 1:**

# Input: arr = {1, 4, 3, -5, -4, 8, 6};
# Output: 8

# **Example 2:**

# Input: arr = {1, 4, 45, 6, 10, -8};
# Output: 45


def findMaxArr(arr,n):
    if n==1:
        return arr[0]

    return max(arr[n-1],findMaxArr(arr, n-1))

print(findMaxArr([1, 4, 45, 6, 10, -8], 6))
