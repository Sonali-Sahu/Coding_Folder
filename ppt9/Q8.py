# Given an array, find a product of all array elements.

# **Example 1:**

# Input  : arr[] = {1, 2, 3, 4, 5}
# Output : 120
# **Example 2:**

# Input  : arr[] = {1, 6, 3}
# Output : 18




def prodArr(arr,n):
    if n == 1:
        return arr[0]

    return arr[n-1]*prodArr(arr, n-1)


print(prodArr([1, 6,3], 3))
