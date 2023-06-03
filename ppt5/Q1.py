# Convert 1D Array Into 2D Array

# You are given a **0-indexed** 1-dimensional (1D) integer array original, and two integers, m and n.
# You are tasked with creating a 2-dimensional (2D) array with  m rows and n columns using **all** the elements from original.

# The elements from indices 0 to n - 1 (**inclusive**) of original should form the first row of the constructed 2D array,
# the elements from indices n to 2 * n - 1 (**inclusive**) should form the second row of the constructed 2D array, and so on.



class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        
        q = []

        for i in range(0, len(original), n):
            q.append(original[i:i+n])
            
        return q
        
